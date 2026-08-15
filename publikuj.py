#!/usr/bin/env python3
"""
Wydanie nowej wersji MarketingAgent do dystrybucji bez gita.

Pakuje każdą wtyczkę do pliku .zip, liczy sumę kontrolną i generuje katalog
`docs/marketplace.json` ze źródłami typu `archive`. Dzięki temu klient instaluje
agenta jedną linijką w oknie Claude Code — bez gita, bez konta GitHub, bez Terminala.

Użycie (z katalogu głównego repozytorium):
    python3 publikuj.py

Potem wystarczy wysłać zmiany:
    git add -A && git commit -m "wydanie X.Y.Z" && git push

Katalog `docs/` jest serwowany przez GitHub Pages pod adresem:
    https://dawlab.github.io/magent/marketplace.json
"""

import hashlib
import json
import shutil
import zipfile
from pathlib import Path

BAZA_URL = "https://dawlab.github.io/magent"
KATALOG_REPO = Path(__file__).parent
KATALOG_WTYCZEK = KATALOG_REPO / "plugins"
KATALOG_WYJSCIA = KATALOG_REPO / "docs"
KATALOG_PACZEK = KATALOG_WYJSCIA / "paczki"

# Pliki pomijane przy pakowaniu
POMIJANE = {".DS_Store", "connectors.example.json.bak"}


def suma_kontrolna(sciezka: Path) -> str:
    h = hashlib.sha256()
    with open(sciezka, "rb") as f:
        for blok in iter(lambda: f.read(65536), b""):
            h.update(blok)
    return h.hexdigest()


def spakuj_wtyczke(katalog: Path, wersja: str) -> Path:
    """Pakuje wtyczkę tak, że w archiwum jest jeden folder najwyższego poziomu."""
    nazwa = katalog.name
    cel = KATALOG_PACZEK / f"{nazwa}-{wersja}.zip"
    with zipfile.ZipFile(cel, "w", zipfile.ZIP_DEFLATED) as z:
        for plik in sorted(katalog.rglob("*")):
            if plik.is_dir() or plik.name in POMIJANE:
                continue
            # ścieżka w archiwum: magent-rdzen/commands/start.md
            z.write(plik, Path(nazwa) / plik.relative_to(katalog))
    return cel


def main() -> None:
    zrodlowy_katalog = KATALOG_REPO / ".claude-plugin" / "marketplace.json"
    katalog_zrodlowy = json.loads(zrodlowy_katalog.read_text(encoding="utf-8"))

    # opisy przepisujemy z istniejącego katalogu, żeby nie rozjechały się teksty
    opisy = {p["name"]: p.get("description", "") for p in katalog_zrodlowy["plugins"]}
    kolejnosc = [p["name"] for p in katalog_zrodlowy["plugins"]]

    if KATALOG_PACZEK.exists():
        shutil.rmtree(KATALOG_PACZEK)
    KATALOG_PACZEK.mkdir(parents=True)

    wtyczki = []
    for nazwa in kolejnosc:
        katalog = KATALOG_WTYCZEK / nazwa
        manifest = katalog / ".claude-plugin" / "plugin.json"
        if not manifest.exists():
            print(f"  POMINIĘTO {nazwa}: brak plugin.json")
            continue

        dane = json.loads(manifest.read_text(encoding="utf-8"))
        wersja = dane["version"]
        paczka = spakuj_wtyczke(katalog, wersja)
        suma = suma_kontrolna(paczka)

        wtyczki.append({
            "name": nazwa,
            "version": wersja,
            "description": opisy.get(nazwa, dane.get("description", "")),
            "source": {
                "source": "archive",
                "url": f"{BAZA_URL}/paczki/{paczka.name}",
                "sha256": suma,
            },
        })
        rozmiar = paczka.stat().st_size / 1024
        print(f"  ✓ {nazwa} {wersja} — {rozmiar:.0f} KB")

    katalog_wyjsciowy = {
        "name": katalog_zrodlowy["name"],
        "owner": katalog_zrodlowy["owner"],
        "metadata": katalog_zrodlowy.get("metadata", {}),
        "plugins": wtyczki,
    }

    (KATALOG_WYJSCIA / "marketplace.json").write_text(
        json.dumps(katalog_wyjsciowy, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    # wyłącza przetwarzanie przez Jekyll na GitHub Pages
    (KATALOG_WYJSCIA / ".nojekyll").write_text("", encoding="utf-8")

    print(f"\nGotowe: {len(wtyczki)} wtyczek w docs/")
    print(f"Adres dla klienta: {BAZA_URL}/marketplace.json")
    print("\nWyślij zmiany:")
    print('  git add -A && git commit -m "wydanie" && git push')


if __name__ == "__main__":
    main()
