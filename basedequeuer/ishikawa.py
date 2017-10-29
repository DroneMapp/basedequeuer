class IshikawaMixin:
    def get_mission(self, mission_id, payload):
        url = self.get_url(f'missions/{mission_id}?_nested=interest_area')
        url = url.format(payload=payload)
        response = self.get(url)
        return response.json()

    def get_region(self, region_id, payload):
        url = self.get_url(f'regions/{region_id}?_nested=coordinates_system_zone')
        url = url.format(payload=payload)
        response = self.get(url)
        return response.json()

    def get_coordinates_system(self, coordinates_system_id, payload):
        url = self.get_url(f'coordinates-systems/{coordinates_system_id}')
        url = url.format(payload=payload)
        response = self.get(url)
        return response.json()

    def get_tileset_for_mission(self, mission_id, payload):
        url = self.get_url(f'tilesets/?ticket__mission_id={mission_id}&type=orthomosaic&_order_by=-created_at&_limit=1&_nested=ticket')
        url = url.format(payload=payload)
        response = self.get(url)
        return response.json()['results'][0]

    def get_polygon_data(self, polygon_id, payload):
        url = self.get_url(f'annotations/polygons/{polygon_id}')
        url = url.format(payload=payload)
        response = self.get(url)
        return response.json()
