# Garbage Man

**Play it: https://petercdavidson.github.io/garbage-man/**

*Garbage Man* is a text adventure I wrote in TI-BASIC on my TI-83/84 Plus in 2009. You're a garbage man. Things go wrong fast.

The web port isn't a rewrite. It runs the original calculator source, line by line, through a small TI-BASIC interpreter on an emulated 96×64 LCD. Play with the on-screen keypad, your keyboard, or by tapping options on the screen.

## Layout

- `TI-BASIC Original/` has the 2009 program (`GARBAGE.8xp`), a plaintext listing, screenshots, and the original readme.
- `web/template.html` is the web port: interpreter, LCD renderer, keypad, death journal.
- `web/build.py` bakes the plaintext listing into the template and writes `docs/index.html`.
- `docs/` is what GitHub Pages serves.

After editing the template, rebuild with:

```bash
python3 web/build.py
```

## Playing on a real calculator

Load `GARBAGE.8xp` onto a TI-83/84 Plus and run `prgmGARBAGE`, or launch it from MirageOS. When in doubt, press ENTER.
