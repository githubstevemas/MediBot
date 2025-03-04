import pandas as pd


def clean_data():
    """
    This function is used to read a raw dataset from the specified CSV file,
    cleaned data then saved into a new CSV file.
    """

    try:
        df = pd.read_csv("data/raw/NTOT2023/NTOT2023_01.CSV",
                         encoding="ISO-8859-1",
                         sep=";",
                         low_memory=False).head(500)

        print("\nCleaning in progress..")

        columns_to_drop = [
            "PRS_FAC_TOP",
            "l_fac_top",
            "l_serie",
            "SERIE",
            "cpl_cod",
            "l_cpl_cod",
            "pre_spe1",
            "l_pre_spe1",
            "pre_stj1",
            "l_pre_stj1",
            "exe_spe1",
            "l_exe_spe1",
            "exe_stj1",
            "l_exe_stj1",
        ]

        df = df.drop(columns=columns_to_drop)

        df['rem_date'] = pd.to_datetime(df['rem_date'], format='%Y%m')
        df['sns_date'] = pd.to_datetime(df['sns_date'], format='%Y%m')

    except Exception as e:
        print(f"Exception: {e}")

    try:
        df.to_csv("data/cleaned/NTOT2023_cleaned.csv",
                  index=False,
                  encoding="ISO-8859-1")

        print("Data successfully cleared!")

    except Exception as e:
        print(e)
