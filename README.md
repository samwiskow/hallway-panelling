# Hallway panelling

A static comparison site for three panelling and dado-rail designs in the hallway and entrance.

- `index.html`: landing page
- `shaker/`, `frames/`, `grooved/`: option pages
- `assets/`: room previews, styles, gallery control and printable cutting pack

GitHub Pages publishes the root of `main`. No build service or external runtime is required. To preview locally, run `python3 -m http.server 8000 --bind 127.0.0.1` from this directory.

Dimensions are planning dimensions. Check final measurements, profiles and service clearances on site. Original survey photographs and Blender source files are kept in the separate modelling project.

Each design has eight hallway views and four entrance views, plus closed, partly open and open barn-door views. The 800 mm open pose is assumed; verify the actual stops. Shallow E1 trim leaves 4–6 mm before adhesive within the measured 15 mm door gap.

The combined 13-page cutting pack covers both rooms. Run `python3 check_site.py` in the public site repository to check links, images, anchors and gallery coverage. GitHub runs the same check for pushes and pull requests.
