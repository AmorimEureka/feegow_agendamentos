import dlt
from source_feegow_agenda import feegow_source

if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="feegow_agenda",
        destination="postgres",
        dataset_name="raw_feegow"
    )

    load_info = pipeline.run(feegow_source())
