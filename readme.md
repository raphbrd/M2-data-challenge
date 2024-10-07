# Master 2 Maths and AI - Data challenges course

This is the main repository for the following two data challenges:
- NYC taxi tip amount prediction
- Forest cover type classification

## Code and data organization
The `data` folder contains the train and test datasets for both challenges.
- Each challenges has 100,000 rows for training and a number of features (see below for full description).
- The test size varies between the two challenges and there is no access to the predictors.

> Preprocessed data are also saved in the `data` folder, but not in the GitHub repo, execute the `preprocessed_*_data.ipynb`
> notebook first.

The `submission` folder contains the csv files submitted to the Kaggle competitions. Submission format:
- NYC taxi tips:
    ```
    row_ID,"tip_amount"
    0,3.5
    1,2.6
    2,4.1
    ...
    ```
- Forest cover type:
    ```
    row_ID,Cover_Type
    0,1
    1,5
    2,7
    3,2
    4,1
    5,1
    ...
    ```

## NYC taxi tips

**Data source:** https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

This is a regression task: the main objective is to predict `tip_amount` in the test dataset.

Features description (from Kaggle):

- `VendorID` - code représentant le fournisseur des données correspondant au trajet (1: Creative Mobile Technologies, 2: VeriFone Inc.)
- `tpep_pickup_datetime` - date et heure de début de la course
- `tpep_dropoff_datetime` - date et heure de fin de la course
- `Passenger_count` - nombre de passagers (indiqué par le conducteur)
- `Trip_distance` - distance correspondant à la course
- `PU_location_lat` - latitude (départ de la course)
- `PU_location_lon` - longitude (départ de la course)
- `DO_location_lat` - latitude (arrivée de la course)
- `DO_location_lon` - longitude (arrivée de la course)
- `RateCodeID` - le type de tarif (1= Standard rate, 2=JFK, 3=Newark, 4=Nassau or Westchester, 5=Negotiated fare, 6=Group ride)
- `Store_and_fwd_flag` - variable binaire indiquant si les informations ont été stocké en mémoire dans le véhicule avant d'être transmises dans le cas où le véhicule n'était pas connecté au réseau (Y=yes, N=no)
- `Payment_type` - type de paiement (1= Credit card, 2= Cash, 3= No charge, 4= Dispute, 5= Unknown, 6= Voided trip)
- `Fare_amount` - tarif de la course sur la base de la distance et du temps
- `Extra` - montant des extras
- `MTA_tax` - taxe MTA
- `Improvement_surcharge` - taxe additionnelle
- `Tolls_amount` - montant des péages payés durant le trajet
- `Congestion_Surcharge` - taxe additionnelle
- `Airport_fee` - frais d'aéroport

## Forest cover type

**<Data source:** https://archive.ics.uci.edu/dataset/31/covertype

This is a classification task: the main objective is to predict the class of `Cover_Type` in the test dataset. The Forest Cover type designation has the following classes (encoded by an Integer between 1 and 7 in the data):
- 1 -- Spruce/Fir
- 2 -- Lodgepole Pine
- 3 -- Ponderosa Pine
- 4 -- Cottonwood/Willow
- 5 -- Aspen
- 6 -- Douglas-fir
- 7 -- Krummholz

Features description:

- `Elevation`: Elevation in meters
- `Aspect`: Azimuth	Aspect in degrees azimuth
- `Slope`: Degrees	Slope in degrees
- `Horizontal_Distance_To_Hydrology`: Horz Dist to nearest surface water features (*in meters*)
- `Vertical_Distance_To_Hydrology`: Vert Dist to nearest surface water features (*in meters*)
- `Horizontal_Distance_To_Roadways`: Horz Dist to nearest roadway (*in meters*)
- `Hillshade_9am`: Hillshade index at 9am, summer solstice (*0 to 255 index*)
- `Hillshade_Noon`: Hillshade index at noon, summer soltice (*0 to 255 index*)
- `Hillshade_3pm`: Hillshade index at 3pm, summer solstice (*0 to 255 index*)
- `Horizontal_Distance_To_Fire_Points`: Horz Dist to nearest wildfire ignition points (*in meters*)
- `Wilderness_Area`: Wilderness area designation. One-hot encoding with 4 binary columns: 0 (absence) or 1 (presence).
    Wilderness Areas:
    - 1 -- Rawah Wilderness Area
    - 2 -- Neota Wilderness Area
    - 3 -- Comanche Peak Wilderness Area
    - 4 -- Cache la Poudre Wilderness Area
- `Soil_Type`: Soil Type designation. One-hot encoding with 40 binary columns: 0 (absence) or 1 (presence). Study Code USFS ELU Code Description:
    - 1 2702 Cathedral family - Rock outcrop complex, extremely stony.
    - 2 2703 Vanet - Ratake families complex, very stony.
    - 3 2704 Haploborolis - Rock outcrop complex, rubbly.
    - 4 2705 Ratake family - Rock outcrop complex, rubbly.
    - 5 2706 Vanet family - Rock outcrop complex complex, rubbly.
    - 6 2717 Vanet - Wetmore families - Rock outcrop complex, stony.
    - 7 3501 Gothic family.
    - 8 3502 Supervisor - Limber families complex.
    - 9 4201 Troutville family, very stony.
    - 10 4703 Bullwark - Catamount families - Rock outcrop complex, rubbly.
    - 11 4704 Bullwark - Catamount families - Rock land complex, rubbly.
    - 12 4744 Legault family - Rock land complex, stony.
    - 13 4758 Catamount family - Rock land - Bullwark family complex, rubbly.
    - 14 5101 Pachic Argiborolis - Aquolis complex.
    - 15 5151 unspecified in the USFS Soil and ELU Survey.
    - 16 6101 Cryaquolis - Cryoborolis complex.
    - 17 6102 Gateview family - Cryaquolis complex.
    - 18 6731 Rogert family, very stony.
    - 19 7101 Typic Cryaquolis - Borohemists complex.
    - 20 7102 Typic Cryaquepts - Typic Cryaquolls complex.
    - 21 7103 Typic Cryaquolls - Leighcan family, till substratum complex.
    - 22 7201 Leighcan family, till substratum, extremely bouldery.
    - 23 7202 Leighcan family, till substratum - Typic Cryaquolls complex.
    - 24 7700 Leighcan family, extremely stony.
    - 25 7701 Leighcan family, warm, extremely stony.
    - 26 7702 Granile - Catamount families complex, very stony.
    - 27 7709 Leighcan family, warm - Rock outcrop complex, extremely stony.
    - 28 7710 Leighcan family - Rock outcrop complex, extremely stony.
    - 29 7745 Como - Legault families complex, extremely stony.
    - 30 7746 Como family - Rock land - Legault family complex, extremely stony.
    - 31 7755 Leighcan - Catamount families complex, extremely stony.
    - 32 7756 Catamount family - Rock outcrop - Leighcan family complex, extremely stony.
    - 33 7757 Leighcan - Catamount families - Rock outcrop complex, extremely stony.
    - 34 7790 Cryorthents - Rock land complex, extremely stony.
    - 35 8703 Cryumbrepts - Rock outcrop - Cryaquepts complex.
    - 36 8707 Bross family - Rock land - Cryumbrepts complex, extremely stony.
    - 37 8708 Rock outcrop - Cryumbrepts - Cryorthents complex, extremely stony.
    - 38 8771 Leighcan - Moran families - Cryaquolls complex, extremely stony.
    - 39 8772 Moran family - Cryorthents - Leighcan family complex, extremely stony.
    - 40 8776 Moran family - Cryorthents - Rock land complex, extremely stony.
