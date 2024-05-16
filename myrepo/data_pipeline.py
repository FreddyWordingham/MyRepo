class DataPipeline:
    def __init__(self, sbi: str):
        self.sbi = sbi

    def best_trees_to_plant(self):
        coord = DataPipeline._sbi_to_coord(self.sbi)
        trees = DataPipeline._esc_api(coord)
        return trees

    @staticmethod
    def _sbi_to_coord(sbi: str):
        if sbi == "exe":
            return (54.2, -2.0)
        else:
            return (0.0, 0.0)

    @staticmethod
    def _esc_api(coord) -> list[str]:
        return ["fern", "apple"]

    def __str__(self):
        return f"SBI: {self.sbi}"
