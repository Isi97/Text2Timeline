import csv
import os


from ..commons.temporal import TemporalEntity
from ..commons.parser_commons import ParserOutput

from typing import Optional


class CSVExporter():

    def __init__(self):
        pass

    def export(self, file_name:str, parser_output: ParserOutput):
        field_names = ["Date", "Year", "Event", "Context_Before", "Context_After"]
        file_name += ".csv"

        script_dir = os.path.dirname(__file__)
        relative_directory = "../../exports"

        parent_output_dir = os.path.normpath(os.path.join(script_dir, relative_directory))

        os.makedirs(parent_output_dir, exist_ok=True)

        file_path = os.path.join(parent_output_dir, file_name)

        with open(file_path, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=field_names)

            writer.writeheader()
            
            for temporal_entity in parser_output.content:
                writer.writerow({
                    "Date": temporal_entity.date,
                    "Year": temporal_entity.year,
                    "Event": temporal_entity.event,
                    "Context_Before": temporal_entity.context_before,
                    "Context_After": temporal_entity.context_after,
                })

        print("Saved to " + file_path)

            