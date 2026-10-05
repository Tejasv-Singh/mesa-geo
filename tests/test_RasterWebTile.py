import unittest

import xyzservices

import mesa_geo as mg


class TestRasterWebTile(unittest.TestCase):
    def test_from_xyzservices(self):
        provider = xyzservices.TileProvider(
            name="Test.Provider",
            url="https://{s}.tiles.example.com/{variant}/{z}/{x}/{y}.png",
            attribution="(C) Example contributors",
            html_attribution='&copy; <a href="https://example.com">Example</a> contributors',
            subdomains="abcd",
            max_zoom=20,
            variant="light_all",
        )
        map_tile = mg.RasterWebTile.from_xyzservices(provider)

        expected_options = {
            "attribution": '&copy; <a href="https://example.com">Example</a> contributors',
            "subdomains": "abcd",
            "max_zoom": 20,
            "variant": "light_all",
            "name": "Test.Provider",
        }
        self.assertEqual(
            map_tile.url, "https://{s}.tiles.example.com/{variant}/{z}/{x}/{y}.png"
        )
        self.assertEqual(map_tile.options, expected_options)
        self.assertEqual(map_tile.kind, "raster_web_tile")
        self.assertEqual(
            map_tile.to_dict(),
            {
                "url": "https://{s}.tiles.example.com/{variant}/{z}/{x}/{y}.png",
                "options": expected_options,
                "kind": "raster_web_tile",
            },
        )

    def test_to_dict(self):
        map_tile = mg.RasterWebTile(
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
            options={
                "attribution": "Map data © <a href='https://openstreetmap.org'>OpenStreetMap</a> contributors"
            },
        )
        self.assertEqual(
            map_tile.to_dict(),
            {
                "kind": "raster_web_tile",
                "url": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                "options": {
                    "attribution": "Map data © <a href='https://openstreetmap.org'>OpenStreetMap</a> contributors",
                },
            },
        )

        map_tile = mg.RasterWebTile(
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        )
        self.assertEqual(
            map_tile.to_dict(),
            {
                "kind": "raster_web_tile",
                "url": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                "options": None,
            },
        )
