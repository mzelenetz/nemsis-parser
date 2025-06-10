EVITALS_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {
        "id": "VitalGroup",
        "table": "evitals_vitalgroup",
        "parent_id": None,
        "type": "group",
    },
    # Direct Children of VitalGroup
    {
        "id": "eVitals.01",
        "table": "evitals_01",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "eVitals.02",
        "table": "evitals_02",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "CardiacRhythmGroup",
        "table": "evitals_cardiacrhythmgroup",
        "parent_id": "VitalGroup",
        "type": "group",
    },
    {
        "id": "BloodPressureGroup",
        "table": "evitals_bloodpressuregroup",
        "parent_id": "VitalGroup",
        "type": "group",
    },
    {
        "id": "HeartRateGroup",
        "table": "evitals_heartrategroup",
        "parent_id": "VitalGroup",
        "type": "group",
    },
    {
        "id": "eVitals.12",
        "table": "evitals_12",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "eVitals.13",
        "table": "evitals_13",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "eVitals.14",
        "table": "evitals_14",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "eVitals.15",
        "table": "evitals_15",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "eVitals.16",
        "table": "evitals_16",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "eVitals.17",
        "table": "evitals_17",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "eVitals.18",
        "table": "evitals_18",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "GlasgowScoreGroup",
        "table": "evitals_glasgowscoregroup",
        "parent_id": "VitalGroup",
        "type": "group",
    },
    {
        "id": "TemperatureGroup",
        "table": "evitals_temperaturegroup",
        "parent_id": "VitalGroup",
        "type": "group",
    },
    {
        "id": "eVitals.26",
        "table": "evitals_26",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "PainScaleGroup",
        "table": "evitals_painscalegroup",
        "parent_id": "VitalGroup",
        "type": "group",
    },
    {
        "id": "StrokeScaleGroup",
        "table": "evitals_strokescalegroup",
        "parent_id": "VitalGroup",
        "type": "group",
    },
    {
        "id": "eVitals.31",
        "table": "evitals_31",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "eVitals.32",
        "table": "evitals_32",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    {
        "id": "eVitals.33",
        "table": "evitals_33",
        "parent_id": "VitalGroup",
        "type": "element",
    },
    # Children of CardiacRhythmGroup
    {
        "id": "eVitals.03",
        "table": "evitals_03",
        "parent_id": "CardiacRhythmGroup",
        "type": "element",
    },
    {
        "id": "eVitals.04",
        "table": "evitals_04",
        "parent_id": "CardiacRhythmGroup",
        "type": "element",
    },
    {
        "id": "eVitals.05",
        "table": "evitals_05",
        "parent_id": "CardiacRhythmGroup",
        "type": "element",
    },
    # Children of BloodPressureGroup
    {
        "id": "eVitals.06",
        "table": "evitals_06",
        "parent_id": "BloodPressureGroup",
        "type": "element",
    },
    {
        "id": "eVitals.07",
        "table": "evitals_07",
        "parent_id": "BloodPressureGroup",
        "type": "element",
    },
    {
        "id": "eVitals.08",
        "table": "evitals_08",
        "parent_id": "BloodPressureGroup",
        "type": "element",
    },
    # Children of HeartRateGroup
    {
        "id": "eVitals.10",
        "table": "evitals_10",
        "parent_id": "HeartRateGroup",
        "type": "element",
    },
    {
        "id": "eVitals.11",
        "table": "evitals_11",
        "parent_id": "HeartRateGroup",
        "type": "element",
    },
    # Children of GlasgowScoreGroup
    {
        "id": "eVitals.19",
        "table": "evitals_19",
        "parent_id": "GlasgowScoreGroup",
        "type": "element",
    },
    {
        "id": "eVitals.20",
        "table": "evitals_20",
        "parent_id": "GlasgowScoreGroup",
        "type": "element",
    },
    {
        "id": "eVitals.21",
        "table": "evitals_21",
        "parent_id": "GlasgowScoreGroup",
        "type": "element",
    },
    {
        "id": "eVitals.22",
        "table": "evitals_22",
        "parent_id": "GlasgowScoreGroup",
        "type": "element",
    },
    {
        "id": "eVitals.23",
        "table": "evitals_23",
        "parent_id": "GlasgowScoreGroup",
        "type": "element",
    },
    # Children of TemperatureGroup
    {
        "id": "eVitals.24",
        "table": "evitals_24",
        "parent_id": "TemperatureGroup",
        "type": "element",
    },
    {
        "id": "eVitals.25",
        "table": "evitals_25",
        "parent_id": "TemperatureGroup",
        "type": "element",
    },
    # Children of PainScaleGroup
    {
        "id": "eVitals.27",
        "table": "evitals_27",
        "parent_id": "PainScaleGroup",
        "type": "element",
    },
    {
        "id": "eVitals.28",
        "table": "evitals_28",
        "parent_id": "PainScaleGroup",
        "type": "element",
    },
    # Children of StrokeScaleGroup
    {
        "id": "eVitals.29",
        "table": "evitals_29",
        "parent_id": "StrokeScaleGroup",
        "type": "element",
    },
    {
        "id": "eVitals.30",
        "table": "evitals_30",
        "parent_id": "StrokeScaleGroup",
        "type": "element",
    },
]

EPROCEDURES_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {"id": "eProcedures", "table": "eprocedures", "parent_id": None, "type": "group"},
    {
        "id": "eProcedures.ProcedureGroup",
        "table": "eprocedures_proceduregroup",
        "parent_id": "eProcedures",
        "type": "group",
    },
    # Direct Children of ProcedureGroup
    {
        "id": "eProcedures.01",
        "table": "eprocedures_01",
        "parent_id": "eProcedures.ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.02",
        "table": "eprocedures_02",
        "parent_id": "eProcedures.ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.03",
        "table": "eprocedures_03",
        "parent_id": "eProcedures.ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.04",
        "table": "eprocedures_04",
        "parent_id": "eProcedures.ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.05",
        "table": "eprocedures_05",
        "parent_id": "eProcedures.ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.06",
        "table": "eprocedures_06",
        "parent_id": "eProcedures.ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.07",
        "table": "eprocedures_07",
        "parent_id": "eProcedures.ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.08",
        "table": "eprocedures_08",
        "parent_id": "eProcedures.ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.09",
        "table": "eprocedures_09",
        "parent_id": "eProcedures.ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.10",
        "table": "eprocedures_10",
        "parent_id": "eProcedures.ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.11",
        "table": "eprocedures_11",
        "parent_id": "eProcedures.ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.12",
        "table": "eprocedures_12",
        "parent_id": "eProcedures.ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.13",
        "table": "eprocedures_13",
        "parent_id": "eProcedures.ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.14",
        "table": "eprocedures_14",
        "parent_id": "eProcedures.ProcedureGroup",
        "type": "element",
    },
    {
        "id": "eProcedures.15",
        "table": "eprocedures_15",
        "parent_id": "eProcedures.ProcedureGroup",
        "type": "element",
    },
]

EAIRWAY_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {
        "id": "AirwayGroup",
        "table": "eairway_airwaygroup",
        "parent_id": None,
        "type": "group",
    },
    # Direct Children of AirwayGroup
    {
        "id": "eAirway.01",
        "table": "eairway_01",
        "parent_id": "AirwayGroup",
        "type": "element",
    },
    {
        "id": "ConfirmationGroup",
        "table": "eairway_confirmationgroup",
        "parent_id": "AirwayGroup",
        "type": "group",
    },
    {
        "id": "eAirway.08",
        "table": "eairway_08",
        "parent_id": "AirwayGroup",
        "type": "element",
    },
    {
        "id": "eAirway.09",
        "table": "eairway_09",
        "parent_id": "AirwayGroup",
        "type": "element",
    },
    {
        "id": "eAirway.10",
        "table": "eairway.10",
        "parent_id": "AirwayGroup",
        "type": "element",
    },
    {
        "id": "eAirway.11",
        "table": "eairway.11",
        "parent_id": "AirwayGroup",
        "type": "element",
    },
    # Children of ConfirmationGroup
    {
        "id": "eAirway.03",
        "table": "eairway_03",
        "parent_id": "ConfirmationGroup",
        "type": "element",
    },
    {
        "id": "eAirway.04",
        "table": "eairway_04",
        "parent_id": "ConfirmationGroup",
        "type": "element",
    },
    {
        "id": "eAirway.05",
        "table": "eairway_05",
        "parent_id": "ConfirmationGroup",
        "type": "element",
    },
    {
        "id": "eAirway.06",
        "table": "eairway_06",
        "parent_id": "ConfirmationGroup",
        "type": "element",
    },
    {
        "id": "eAirway.07",
        "table": "eairway_07",
        "parent_id": "ConfirmationGroup",
        "type": "element",
    },
]

ECREW_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {
        "id": "CrewGroup",
        "table": "ecrew_crewgroup",
        "parent_id": None,
        "type": "group",
    },
    # Direct Children of CrewGroup
    {
        "id": "eCrew.01",
        "table": "ecrew_01",
        "parent_id": "CrewGroup",
        "type": "element",
    },
    {
        "id": "eCrew.02",
        "table": "ecrew_02",
        "parent_id": "CrewGroup",
        "type": "element",
    },
    {
        "id": "eCrew.03",
        "table": "ecrew_03",
        "parent_id": "CrewGroup",
        "type": "element",
    },
]

EDEVICE_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {
        "id": "DeviceGroup",
        "table": "edevice_devicegroup",
        "parent_id": None,
        "type": "group",
    },
    # Direct Children of DeviceGroup
    {
        "id": "eDevice.01",
        "table": "edevice_01",
        "parent_id": "DeviceGroup",
        "type": "element",
    },
    {
        "id": "eDevice.02",
        "table": "edevice_02",
        "parent_id": "DeviceGroup",
        "type": "element",
    },
    {
        "id": "eDevice.03",
        "table": "edevice_03",
        "parent_id": "DeviceGroup",
        "type": "element",
    },
    {
        "id": "eDevice.07",
        "table": "edevice_07",
        "parent_id": "DeviceGroup",
        "type": "element",
    },
    {
        "id": "eDevice.08",
        "table": "edevice_08",
        "parent_id": "DeviceGroup",
        "type": "element",
    },
    {
        "id": "ShockGroup",
        "table": "edevice_shockgroup",
        "parent_id": "DeviceGroup",
        "type": "group",
    },
    {
        "id": "WaveformGroup",
        "table": "edevice_waveformgroup",
        "parent_id": "DeviceGroup",
        "type": "group",
    },
    # Direct Children of DeviceGroup
    {
        "id": "eDevice.04",
        "table": "edevice_04",
        "parent_id": "WaveformGroup",
        "type": "element",
    },
    {
        "id": "eDevice.05",
        "table": "edevice_05",
        "parent_id": "WaveformGroup",
        "type": "element",
    },
    {
        "id": "eDevice.06",
        "table": "edevice_06",
        "parent_id": "WaveformGroup",
        "type": "element",
    },
    # Direct Children of ShockGroup
    {
        "id": "eDevice.09",
        "table": "edevice_09",
        "parent_id": "ShockGroup",
        "type": "element",
    },
    {
        "id": "eDevice.10",
        "table": "edevice_10",
        "parent_id": "ShockGroup",
        "type": "element",
    },
    {
        "id": "eDevice.11",
        "table": "edevice_11",
        "parent_id": "ShockGroup",
        "type": "element",
    },
    {
        "id": "eDevice.12",
        "table": "edevice_12",
        "parent_id": "ShockGroup",
        "type": "element",
    },
]

EARREST_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {
        "id": "eArrest",
        "table": "earrest",
        "parent_id": None,
        "type": "group",
    },
    # Direct Children of eArrest
    {
        "id": "eArrest.01",
        "table": "earrest_01",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.02",
        "table": "earrest_02",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.03",
        "table": "earrest_03",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.04",
        "table": "earrest_04",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.05",
        "table": "earrest_05",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.06",
        "table": "earrest_06",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.07",
        "table": "earrest_07",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.08",
        "table": "earrest_08",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.09",
        "table": "earrest_09",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.10",
        "table": "earrest_10",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.11",
        "table": "earrest_11",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.12",
        "table": "earrest_12",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.13",
        "table": "earrest_13",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.14",
        "table": "earrest_14",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.15",
        "table": "earrest_15",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.16",
        "table": "earrest_16",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.17",
        "table": "earrest_17",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.18",
        "table": "earrest_18",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.19",
        "table": "earrest_19",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.20",
        "table": "earrest_20",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.21",
        "table": "earrest_21",
        "parent_id": "eArrest",
        "type": "element",
    },
    {
        "id": "eArrest.22",
        "table": "earrest_22",
        "parent_id": "eArrest",
        "type": "element",
    },
]

EDISPATCH_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {
        "id": "eDispatch",
        "table": "edispatch",
        "parent_id": None,
        "type": "group",
    },
    # Direct Children of eDispatch
    {
        "id": "eDispatch.01",
        "table": "edispatch_01",
        "parent_id": "eDispatch",
        "type": "element",
    },
    {
        "id": "eDispatch.02",
        "table": "edispatch_02",
        "parent_id": "eDispatch",
        "type": "element",
    },
    {
        "id": "eDispatch.03",
        "table": "edispatch_03",
        "parent_id": "eDispatch",
        "type": "element",
    },
    {
        "id": "eDispatch.04",
        "table": "edispatch_04",
        "parent_id": "eDispatch",
        "type": "element",
    },
    {
        "id": "eDispatch.05",
        "table": "edispatch_05",
        "parent_id": "eDispatch",
        "type": "element",
    },
    {
        "id": "eDispatch.06",
        "table": "edispatch_06",
        "parent_id": "eDispatch",
        "type": "element",
    },
]

EDISPOSITION_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {
        "id": "eDisposition",
        "table": "edisposition",
        "parent_id": None,
        "type": "group",
    },
    # DestinationGroup
    {
        "id": "eDisposition.DestinationGroup",
        "table": "edisposition_destinationgroup",
        "parent_id": "eDisposition",
        "type": "group",
    },
    {
        "id": "eDisposition.01",
        "table": "edisposition_01",
        "parent_id": "eDisposition.DestinationGroup",
        "type": "element",
    },
    {
        "id": "eDisposition.02",
        "table": "edisposition_02",
        "parent_id": "eDisposition.DestinationGroup",
        "type": "element",
    },
    {
        "id": "eDisposition.03",
        "table": "edisposition_03",
        "parent_id": "eDisposition.DestinationGroup",
        "type": "element",
    },
    {
        "id": "eDisposition.04",
        "table": "edisposition_04",
        "parent_id": "eDisposition.DestinationGroup",
        "type": "element",
    },
    {
        "id": "eDisposition.05",
        "table": "edisposition_05",
        "parent_id": "eDisposition.DestinationGroup",
        "type": "element",
    },
    {
        "id": "eDisposition.06",
        "table": "edisposition_06",
        "parent_id": "eDisposition.DestinationGroup",
        "type": "element",
    },
    {
        "id": "eDisposition.07",
        "table": "edisposition_07",
        "parent_id": "eDisposition.DestinationGroup",
        "type": "element",
    },
    {
        "id": "eDisposition.08",
        "table": "edisposition_08",
        "parent_id": "eDisposition.DestinationGroup",
        "type": "element",
    },
    {
        "id": "eDisposition.09",
        "table": "edisposition_09",
        "parent_id": "eDisposition.DestinationGroup",
        "type": "element",
    },
    {
        "id": "eDisposition.10",
        "table": "edisposition_10",
        "parent_id": "eDisposition.DestinationGroup",
        "type": "element",
    },
    # Direct child of eDisposition
    {
        "id": "eDisposition.11",
        "table": "edisposition_11",
        "parent_id": "eDisposition",
        "type": "element",
    },
    # IncidentDispositionGroup
    {
        "id": "eDisposition.IncidentDispositionGroup",
        "table": "edisposition_incidentdispositiongroup",
        "parent_id": "eDisposition",
        "type": "group",
    },
    {
        "id": "eDisposition.27",
        "table": "edisposition_27",
        "parent_id": "eDisposition.IncidentDispositionGroup",
        "type": "element",
    },
    {
        "id": "eDisposition.28",
        "table": "edisposition_28",
        "parent_id": "eDisposition.IncidentDispositionGroup",
        "type": "element",
    },
    {
        "id": "eDisposition.29",
        "table": "edisposition_29",
        "parent_id": "eDisposition.IncidentDispositionGroup",
        "type": "element",
    },
    {
        "id": "eDisposition.30",
        "table": "edisposition_30",
        "parent_id": "eDisposition.IncidentDispositionGroup",
        "type": "element",
    },
    {
        "id": "eDisposition.31",
        "table": "edisposition_31",
        "parent_id": "eDisposition.IncidentDispositionGroup",
        "type": "element",
    },
    # More direct children of eDisposition
    {
        "id": "eDisposition.13",
        "table": "edisposition_13",
        "parent_id": "eDisposition",
        "type": "element",
    },
    {
        "id": "eDisposition.14",
        "table": "edisposition_14",
        "parent_id": "eDisposition",
        "type": "element",
    },
    {
        "id": "eDisposition.15",
        "table": "edisposition_15",
        "parent_id": "eDisposition",
        "type": "element",
    },
    {
        "id": "eDisposition.16",
        "table": "edisposition_16",
        "parent_id": "eDisposition",
        "type": "element",
    },
    {
        "id": "eDisposition.17",
        "table": "edisposition_17",
        "parent_id": "eDisposition",
        "type": "element",
    },
    {
        "id": "eDisposition.18",
        "table": "edisposition_18",
        "parent_id": "eDisposition",
        "type": "element",
    },
    {
        "id": "eDisposition.19",
        "table": "edisposition_19",
        "parent_id": "eDisposition",
        "type": "element",
    },
    {
        "id": "eDisposition.20",
        "table": "edisposition_20",
        "parent_id": "eDisposition",
        "type": "element",
    },
    {
        "id": "eDisposition.21",
        "table": "edisposition_21",
        "parent_id": "eDisposition",
        "type": "element",
    },
    {
        "id": "eDisposition.22",
        "table": "edisposition_22",
        "parent_id": "eDisposition",
        "type": "element",
    },
    {
        "id": "eDisposition.23",
        "table": "edisposition_23",
        "parent_id": "eDisposition",
        "type": "element",
    },
    # HospitalTeamActivationGroup
    {
        "id": "eDisposition.HospitalTeamActivationGroup",
        "table": "edisposition_hospitalteamactivationgroup",
        "parent_id": "eDisposition",
        "type": "group",
    },
    {
        "id": "eDisposition.24",
        "table": "edisposition_24",
        "parent_id": "eDisposition.HospitalTeamActivationGroup",
        "type": "element",
    },
    {
        "id": "eDisposition.25",
        "table": "edisposition_25",
        "parent_id": "eDisposition.HospitalTeamActivationGroup",
        "type": "element",
    },
    # More direct children of eDisposition
    {
        "id": "eDisposition.26",
        "table": "edisposition_26",
        "parent_id": "eDisposition",
        "type": "element",
    },
    {
        "id": "eDisposition.32",
        "table": "edisposition_32",
        "parent_id": "eDisposition",
        "type": "element",
    },
]

EEXAM_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {"id": "eExam", "table": "eexam", "parent_id": None, "type": "group"},
    # Direct elements of eExam
    {"id": "eExam.01", "table": "eexam_01", "parent_id": "eExam", "type": "element"},
    {"id": "eExam.02", "table": "eexam_02", "parent_id": "eExam", "type": "element"},
    # AssessmentGroup
    {
        "id": "eExam.AssessmentGroup",
        "table": "eexam_assessmentgroup",
        "parent_id": "eExam",
        "type": "group",
    },
    {
        "id": "eExam.03",
        "table": "eexam_03",
        "parent_id": "eExam.AssessmentGroup",
        "type": "element",
    },
    {
        "id": "eExam.04",
        "table": "eexam_04",
        "parent_id": "eExam.AssessmentGroup",
        "type": "element",
    },
    {
        "id": "eExam.05",
        "table": "eexam_05",
        "parent_id": "eExam.AssessmentGroup",
        "type": "element",
    },
    {
        "id": "eExam.06",
        "table": "eexam_06",
        "parent_id": "eExam.AssessmentGroup",
        "type": "element",
    },
    {
        "id": "eExam.07",
        "table": "eexam_07",
        "parent_id": "eExam.AssessmentGroup",
        "type": "element",
    },
    {
        "id": "eExam.08",
        "table": "eexam_08",
        "parent_id": "eExam.AssessmentGroup",
        "type": "element",
    },
    {
        "id": "eExam.09",
        "table": "eexam_09",
        "parent_id": "eExam.AssessmentGroup",
        "type": "element",
    },
    # AbdomenGroup
    {
        "id": "eExam.AbdomenGroup",
        "table": "eexam_abdomengroup",
        "parent_id": "eExam.AssessmentGroup",
        "type": "group",
    },
    {
        "id": "eExam.10",
        "table": "eexam_10",
        "parent_id": "eExam.AbdomenGroup",
        "type": "element",
    },
    {
        "id": "eExam.11",
        "table": "eexam_11",
        "parent_id": "eExam.AbdomenGroup",
        "type": "element",
    },
    # Pelvis/Genitourinary Assessment (direct child of AssessmentGroup)
    {
        "id": "eExam.12",
        "table": "eexam_12",
        "parent_id": "eExam.AssessmentGroup",
        "type": "element",
    },
    # SpineGroup
    {
        "id": "eExam.SpineGroup",
        "table": "eexam_spinegroup",
        "parent_id": "eExam.AssessmentGroup",
        "type": "group",
    },
    {
        "id": "eExam.13",
        "table": "eexam_13",
        "parent_id": "eExam.SpineGroup",
        "type": "element",
    },
    {
        "id": "eExam.14",
        "table": "eexam_14",
        "parent_id": "eExam.SpineGroup",
        "type": "element",
    },
    # ExtremityGroup
    {
        "id": "eExam.ExtremityGroup",
        "table": "eexam_extremitygroup",
        "parent_id": "eExam.AssessmentGroup",
        "type": "group",
    },
    {
        "id": "eExam.15",
        "table": "eexam_15",
        "parent_id": "eExam.ExtremityGroup",
        "type": "element",
    },
    {
        "id": "eExam.16",
        "table": "eexam_16",
        "parent_id": "eExam.ExtremityGroup",
        "type": "element",
    },
    # EyeGroup
    {
        "id": "eExam.EyeGroup",
        "table": "eexam_eyegroup",
        "parent_id": "eExam.AssessmentGroup",
        "type": "group",
    },
    {
        "id": "eExam.17",
        "table": "eexam_17",
        "parent_id": "eExam.EyeGroup",
        "type": "element",
    },
    {
        "id": "eExam.18",
        "table": "eexam_18",
        "parent_id": "eExam.EyeGroup",
        "type": "element",
    },
    # LungGroup
    {
        "id": "eExam.LungGroup",
        "table": "eexam_lunggroup",
        "parent_id": "eExam.AssessmentGroup",
        "type": "group",
    },
    {
        "id": "eExam.22",
        "table": "eexam_22",
        "parent_id": "eExam.LungGroup",
        "type": "element",
    },
    {
        "id": "eExam.23",
        "table": "eexam_23",
        "parent_id": "eExam.LungGroup",
        "type": "element",
    },
    # ChestGroup
    {
        "id": "eExam.ChestGroup",
        "table": "eexam_chestgroup",
        "parent_id": "eExam.AssessmentGroup",
        "type": "group",
    },
    {
        "id": "eExam.24",
        "table": "eexam_24",
        "parent_id": "eExam.ChestGroup",
        "type": "element",
    },
    {
        "id": "eExam.25",
        "table": "eexam_25",
        "parent_id": "eExam.ChestGroup",
        "type": "element",
    },
    # More direct elements of eExam
    {"id": "eExam.20", "table": "eexam_20", "parent_id": "eExam", "type": "element"},
    {"id": "eExam.21", "table": "eexam_21", "parent_id": "eExam", "type": "element"},
]

EHISTORY_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {"id": "eHistory", "table": "ehistory", "parent_id": None, "type": "group"},
    # Direct elements of eHistory
    {
        "id": "eHistory.01",
        "table": "ehistory_01",
        "parent_id": "eHistory",
        "type": "element",
    },
    {
        "id": "eHistory.05",
        "table": "ehistory_05",
        "parent_id": "eHistory",
        "type": "element",
    },
    {
        "id": "eHistory.06",
        "table": "ehistory_06",
        "parent_id": "eHistory",
        "type": "element",
    },
    {
        "id": "eHistory.07",
        "table": "ehistory_07",
        "parent_id": "eHistory",
        "type": "element",
    },
    {
        "id": "eHistory.08",
        "table": "ehistory_08",
        "parent_id": "eHistory",
        "type": "element",
    },
    {
        "id": "eHistory.09",
        "table": "ehistory_09",
        "parent_id": "eHistory",
        "type": "element",
    },
    {
        "id": "eHistory.16",
        "table": "ehistory_16",
        "parent_id": "eHistory",
        "type": "element",
    },
    {
        "id": "eHistory.17",
        "table": "ehistory_17",
        "parent_id": "eHistory",
        "type": "element",
    },
    {
        "id": "eHistory.18",
        "table": "ehistory_18",
        "parent_id": "eHistory",
        "type": "element",
    },
    {
        "id": "eHistory.19",
        "table": "ehistory_19",
        "parent_id": "eHistory",
        "type": "element",
    },
    # PractitionerGroup
    {
        "id": "eHistory.PractitionerGroup",
        "table": "ehistory_practitionergroup",
        "parent_id": "eHistory",
        "type": "group",
    },
    {
        "id": "eHistory.02",
        "table": "ehistory_02",
        "parent_id": "eHistory.PractitionerGroup",
        "type": "element",
    },
    {
        "id": "eHistory.03",
        "table": "ehistory_03",
        "parent_id": "eHistory.PractitionerGroup",
        "type": "element",
    },
    {
        "id": "eHistory.04",
        "table": "ehistory_04",
        "parent_id": "eHistory.PractitionerGroup",
        "type": "element",
    },
    # ImmunizationsGroup
    {
        "id": "eHistory.ImmunizationsGroup",
        "table": "ehistory_immunizationsgroup",
        "parent_id": "eHistory",
        "type": "group",
    },
    {
        "id": "eHistory.10",
        "table": "ehistory_10",
        "parent_id": "eHistory.ImmunizationsGroup",
        "type": "element",
    },
    {
        "id": "eHistory.11",
        "table": "ehistory_11",
        "parent_id": "eHistory.ImmunizationsGroup",
        "type": "element",
    },
    # CurrentMedsGroup
    {
        "id": "eHistory.CurrentMedsGroup",
        "table": "ehistory_currentmedsgroup",
        "parent_id": "eHistory",
        "type": "group",
    },
    {
        "id": "eHistory.12",
        "table": "ehistory_12",
        "parent_id": "eHistory.CurrentMedsGroup",
        "type": "element",
    },
    {
        "id": "eHistory.13",
        "table": "ehistory_13",
        "parent_id": "eHistory.CurrentMedsGroup",
        "type": "element",
    },
    {
        "id": "eHistory.14",
        "table": "ehistory_14",
        "parent_id": "eHistory.CurrentMedsGroup",
        "type": "element",
    },
    {
        "id": "eHistory.15",
        "table": "ehistory_15",
        "parent_id": "eHistory.CurrentMedsGroup",
        "type": "element",
    },
    {
        "id": "eHistory.20",
        "table": "ehistory_20",
        "parent_id": "eHistory.CurrentMedsGroup",
        "type": "element",
    },
]

EINJURY_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {"id": "eInjury", "table": "einjury", "parent_id": None, "type": "group"},
    # Direct elements of eInjury
    {
        "id": "eInjury.01",
        "table": "einjury_01",
        "parent_id": "eInjury",
        "type": "element",
    },
    {
        "id": "eInjury.02",
        "table": "einjury_02",
        "parent_id": "eInjury",
        "type": "element",
    },
    {
        "id": "eInjury.03",
        "table": "einjury_03",
        "parent_id": "eInjury",
        "type": "element",
    },
    {
        "id": "eInjury.04",
        "table": "einjury_04",
        "parent_id": "eInjury",
        "type": "element",
    },
    {
        "id": "eInjury.05",
        "table": "einjury_05",
        "parent_id": "eInjury",
        "type": "element",
    },
    {
        "id": "eInjury.06",
        "table": "einjury_06",
        "parent_id": "eInjury",
        "type": "element",
    },
    {
        "id": "eInjury.07",
        "table": "einjury_07",
        "parent_id": "eInjury",
        "type": "element",
    },
    {
        "id": "eInjury.08",
        "table": "einjury_08",
        "parent_id": "eInjury",
        "type": "element",
    },
    {
        "id": "eInjury.09",
        "table": "einjury_09",
        "parent_id": "eInjury",
        "type": "element",
    },
    {
        "id": "eInjury.10",
        "table": "einjury_10",
        "parent_id": "eInjury",
        "type": "element",
    },
    # CollisionGroup
    {
        "id": "eInjury.CollisionGroup",
        "table": "einjury_collisiongroup",
        "parent_id": "eInjury",
        "type": "group",
    },
    {
        "id": "eInjury.11",
        "table": "einjury_11",
        "parent_id": "eInjury.CollisionGroup",
        "type": "element",
    },
    {
        "id": "eInjury.12",
        "table": "einjury_12",
        "parent_id": "eInjury.CollisionGroup",
        "type": "element",
    },
    {
        "id": "eInjury.13",
        "table": "einjury_13",
        "parent_id": "eInjury.CollisionGroup",
        "type": "element",
    },
    {
        "id": "eInjury.14",
        "table": "einjury_14",
        "parent_id": "eInjury.CollisionGroup",
        "type": "element",
    },
    {
        "id": "eInjury.15",
        "table": "einjury_15",
        "parent_id": "eInjury.CollisionGroup",
        "type": "element",
    },
    {
        "id": "eInjury.16",
        "table": "einjury_16",
        "parent_id": "eInjury.CollisionGroup",
        "type": "element",
    },
    {
        "id": "eInjury.17",
        "table": "einjury_17",
        "parent_id": "eInjury.CollisionGroup",
        "type": "element",
    },
    {
        "id": "eInjury.18",
        "table": "einjury_18",
        "parent_id": "eInjury.CollisionGroup",
        "type": "element",
    },
    {
        "id": "eInjury.19",
        "table": "einjury_19",
        "parent_id": "eInjury.CollisionGroup",
        "type": "element",
    },
    {
        "id": "eInjury.20",
        "table": "einjury_20",
        "parent_id": "eInjury.CollisionGroup",
        "type": "element",
    },
    {
        "id": "eInjury.21",
        "table": "einjury_21",
        "parent_id": "eInjury.CollisionGroup",
        "type": "element",
    },
    {
        "id": "eInjury.22",
        "table": "einjury_22",
        "parent_id": "eInjury.CollisionGroup",
        "type": "element",
    },
    {
        "id": "eInjury.23",
        "table": "einjury_23",
        "parent_id": "eInjury.CollisionGroup",
        "type": "element",
    },
    {
        "id": "eInjury.24",
        "table": "einjury_24",
        "parent_id": "eInjury.CollisionGroup",
        "type": "element",
    },
    {
        "id": "eInjury.25",
        "table": "einjury_25",
        "parent_id": "eInjury.CollisionGroup",
        "type": "element",
    },
    # SeatGroup
    {
        "id": "eInjury.SeatGroup",
        "table": "einjury_seatgroup",
        "parent_id": "eInjury.CollisionGroup",
        "type": "group",
    },
    {
        "id": "eInjury.26",
        "table": "einjury_26",
        "parent_id": "eInjury.SeatGroup",
        "type": "element",
    },
    {
        "id": "eInjury.27",
        "table": "einjury_27",
        "parent_id": "eInjury.SeatGroup",
        "type": "element",
    },
    {
        "id": "eInjury.28",
        "table": "einjury_28",
        "parent_id": "eInjury.SeatGroup",
        "type": "element",
    },
    {
        "id": "eInjury.29",
        "table": "einjury_29",
        "parent_id": "eInjury.SeatGroup",
        "type": "element",
    },
]

ELABS_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {"id": "eLabs", "table": "elabs", "parent_id": None, "type": "group"},
    # LabGroup
    {
        "id": "eLabs.LabGroup",
        "table": "elabs_labgroup",
        "parent_id": "eLabs",
        "type": "group",
    },
    {
        "id": "eLabs.01",
        "table": "elabs_01",
        "parent_id": "eLabs.LabGroup",
        "type": "element",
    },
    {
        "id": "eLabs.02",
        "table": "elabs_02",
        "parent_id": "eLabs.LabGroup",
        "type": "element",
    },
    # LabResultGroup
    {
        "id": "eLabs.LabResultGroup",
        "table": "elabs_labresultgroup",
        "parent_id": "eLabs.LabGroup",
        "type": "group",
    },
    {
        "id": "eLabs.03",
        "table": "elabs_03",
        "parent_id": "eLabs.LabResultGroup",
        "type": "element",
    },
    {
        "id": "eLabs.04",
        "table": "elabs_04",
        "parent_id": "eLabs.LabResultGroup",
        "type": "element",
    },
    # LabImageGroup
    {
        "id": "eLabs.LabImageGroup",
        "table": "elabs_labimagegroup",
        "parent_id": "eLabs.LabGroup",
        "type": "group",
    },
    {
        "id": "eLabs.05",
        "table": "elabs_05",
        "parent_id": "eLabs.LabImageGroup",
        "type": "element",
    },
    {
        "id": "eLabs.06",
        "table": "elabs_06",
        "parent_id": "eLabs.LabImageGroup",
        "type": "element",
    },
    # WaveformGraphicGroup
    {
        "id": "eLabs.WaveformGraphicGroup",
        "table": "elabs_waveformgraphicgroup",
        "parent_id": "eLabs.LabImageGroup",
        "type": "group",
    },
    {
        "id": "eLabs.07",
        "table": "elabs_07",
        "parent_id": "eLabs.WaveformGraphicGroup",
        "type": "element",
    },
    {
        "id": "eLabs.08",
        "table": "elabs_08",
        "parent_id": "eLabs.WaveformGraphicGroup",
        "type": "element",
    },
]

EMEDICATIONS_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {"id": "eMedications", "table": "emedications", "parent_id": None, "type": "group"},
    # MedicationGroup
    {
        "id": "eMedications.MedicationGroup",
        "table": "emedications_medicationgroup",
        "parent_id": "eMedications",
        "type": "group",
    },
    {
        "id": "eMedications.01",
        "table": "emedications_01",
        "parent_id": "eMedications.MedicationGroup",
        "type": "element",
    },
    {
        "id": "eMedications.02",
        "table": "emedications_02",
        "parent_id": "eMedications.MedicationGroup",
        "type": "element",
    },
    {
        "id": "eMedications.03",
        "table": "emedications_03",
        "parent_id": "eMedications.MedicationGroup",
        "type": "element",
    },
    {
        "id": "eMedications.04",
        "table": "emedications_04",
        "parent_id": "eMedications.MedicationGroup",
        "type": "element",
    },
    # DosageGroup
    {
        "id": "eMedications.DosageGroup",
        "table": "emedications_dosagegroup",
        "parent_id": "eMedications.MedicationGroup",
        "type": "group",
    },
    {
        "id": "eMedications.05",
        "table": "emedications_05",
        "parent_id": "eMedications.DosageGroup",
        "type": "element",
    },
    {
        "id": "eMedications.06",
        "table": "emedications_06",
        "parent_id": "eMedications.DosageGroup",
        "type": "element",
    },
    {
        "id": "eMedications.07",
        "table": "emedications_07",
        "parent_id": "eMedications.MedicationGroup",
        "type": "element",
    },
    {
        "id": "eMedications.08",
        "table": "emedications_08",
        "parent_id": "eMedications.MedicationGroup",
        "type": "element",
    },
    {
        "id": "eMedications.09",
        "table": "emedications_09",
        "parent_id": "eMedications.MedicationGroup",
        "type": "element",
    },
    {
        "id": "eMedications.10",
        "table": "emedications_10",
        "parent_id": "eMedications.MedicationGroup",
        "type": "element",
    },
    {
        "id": "eMedications.11",
        "table": "emedications_11",
        "parent_id": "eMedications.MedicationGroup",
        "type": "element",
    },
    {
        "id": "eMedications.12",
        "table": "emedications_12",
        "parent_id": "eMedications.MedicationGroup",
        "type": "element",
    },
    {
        "id": "eMedications.13",
        "table": "emedications_13",
        "parent_id": "eMedications.MedicationGroup",
        "type": "element",
    },
]

EOTHER_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {"id": "eOther", "table": "eother", "parent_id": None, "type": "group"},
    # Direct elements of eOther
    {"id": "eOther.01", "table": "eother_01", "parent_id": "eOther", "type": "element"},
    {"id": "eOther.02", "table": "eother_02", "parent_id": "eOther", "type": "element"},
    {"id": "eOther.07", "table": "eother_07", "parent_id": "eOther", "type": "element"},
    {"id": "eOther.08", "table": "eother_08", "parent_id": "eOther", "type": "element"},
    # EMSCrewMemberGroup
    {
        "id": "eOther.EMSCrewMemberGroup",
        "table": "eother_emscrewmembergroup",
        "parent_id": "eOther",
        "type": "group",
    },
    {
        "id": "eOther.03",
        "table": "eother_03",
        "parent_id": "eOther.EMSCrewMemberGroup",
        "type": "element",
    },
    {
        "id": "eOther.04",
        "table": "eother_04",
        "parent_id": "eOther.EMSCrewMemberGroup",
        "type": "element",
    },
    {
        "id": "eOther.05",
        "table": "eother_05",
        "parent_id": "eOther.EMSCrewMemberGroup",
        "type": "element",
    },
    {
        "id": "eOther.06",
        "table": "eother_06",
        "parent_id": "eOther.EMSCrewMemberGroup",
        "type": "element",
    },
    # FileGroup
    {
        "id": "eOther.FileGroup",
        "table": "eother_filegroup",
        "parent_id": "eOther",
        "type": "group",
    },
    {
        "id": "eOther.09",
        "table": "eother_09",
        "parent_id": "eOther.FileGroup",
        "type": "element",
    },
    {
        "id": "eOther.10",
        "table": "eother_10",
        "parent_id": "eOther.FileGroup",
        "type": "element",
    },
    {
        "id": "eOther.11",
        "table": "eother_11",
        "parent_id": "eOther.FileGroup",
        "type": "element",
    },
    {
        "id": "eOther.22",
        "table": "eother_22",
        "parent_id": "eOther.FileGroup",
        "type": "element",
    },
    # SignatureGroup
    {
        "id": "eOther.SignatureGroup",
        "table": "eother_signaturegroup",
        "parent_id": "eOther",
        "type": "group",
    },
    {
        "id": "eOther.12",
        "table": "eother_12",
        "parent_id": "eOther.SignatureGroup",
        "type": "element",
    },
    {
        "id": "eOther.13",
        "table": "eother_13",
        "parent_id": "eOther.SignatureGroup",
        "type": "element",
    },
    {
        "id": "eOther.14",
        "table": "eother_14",
        "parent_id": "eOther.SignatureGroup",
        "type": "element",
    },
    {
        "id": "eOther.15",
        "table": "eother_15",
        "parent_id": "eOther.SignatureGroup",
        "type": "element",
    },
    {
        "id": "eOther.16",
        "table": "eother_16",
        "parent_id": "eOther.SignatureGroup",
        "type": "element",
    },
    {
        "id": "eOther.17",
        "table": "eother_17",
        "parent_id": "eOther.SignatureGroup",
        "type": "element",
    },
    {
        "id": "eOther.18",
        "table": "eother_18",
        "parent_id": "eOther.SignatureGroup",
        "type": "element",
    },
    {
        "id": "eOther.19",
        "table": "eother_19",
        "parent_id": "eOther.SignatureGroup",
        "type": "element",
    },
    {
        "id": "eOther.20",
        "table": "eother_20",
        "parent_id": "eOther.SignatureGroup",
        "type": "element",
    },
    {
        "id": "eOther.21",
        "table": "eother_21",
        "parent_id": "eOther.SignatureGroup",
        "type": "element",
    },
]

EOUTCOME_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {"id": "eOutcome", "table": "eoutcome", "parent_id": None, "type": "group"},
    # Direct elements of eOutcome
    {
        "id": "eOutcome.01",
        "table": "eoutcome_01",
        "parent_id": "eOutcome",
        "type": "element",
    },
    {
        "id": "eOutcome.02",
        "table": "eoutcome_02",
        "parent_id": "eOutcome",
        "type": "element",
    },
    # ExternalDataGroup
    {
        "id": "eOutcome.ExternalDataGroup",
        "table": "eoutcome_externaldatagroup",
        "parent_id": "eOutcome",
        "type": "group",
    },
    {
        "id": "eOutcome.03",
        "table": "eoutcome_03",
        "parent_id": "eOutcome.ExternalDataGroup",
        "type": "element",
    },
    {
        "id": "eOutcome.04",
        "table": "eoutcome_04",
        "parent_id": "eOutcome.ExternalDataGroup",
        "type": "element",
    },
    {
        "id": "eOutcome.05",
        "table": "eoutcome_05",
        "parent_id": "eOutcome.ExternalDataGroup",
        "type": "element",
    },
    # EmergencyDepartmentProceduresGroup
    {
        "id": "eOutcome.EmergencyDepartmentProceduresGroup",
        "table": "eoutcome_emergencydepartmentproceduresgroup",
        "parent_id": "eOutcome",
        "type": "group",
    },
    {
        "id": "eOutcome.09",
        "table": "eoutcome_09",
        "parent_id": "eOutcome.EmergencyDepartmentProceduresGroup",
        "type": "element",
    },
    {
        "id": "eOutcome.19",
        "table": "eoutcome_19",
        "parent_id": "eOutcome.EmergencyDepartmentProceduresGroup",
        "type": "element",
    },
    # More direct elements of eOutcome
    {
        "id": "eOutcome.10",
        "table": "eoutcome_10",
        "parent_id": "eOutcome",
        "type": "element",
    },
    {
        "id": "eOutcome.11",
        "table": "eoutcome_11",
        "parent_id": "eOutcome",
        "type": "element",
    },
    # HospitalProceduresGroup
    {
        "id": "eOutcome.HospitalProceduresGroup",
        "table": "eoutcome_hospitalproceduresgroup",
        "parent_id": "eOutcome",
        "type": "group",
    },
    {
        "id": "eOutcome.12",
        "table": "eoutcome_12",
        "parent_id": "eOutcome.HospitalProceduresGroup",
        "type": "element",
    },
    {
        "id": "eOutcome.20",
        "table": "eoutcome_20",
        "parent_id": "eOutcome.HospitalProceduresGroup",
        "type": "element",
    },
    # More direct elements of eOutcome
    {
        "id": "eOutcome.13",
        "table": "eoutcome_13",
        "parent_id": "eOutcome",
        "type": "element",
    },
    {
        "id": "eOutcome.16",
        "table": "eoutcome_16",
        "parent_id": "eOutcome",
        "type": "element",
    },
    {
        "id": "eOutcome.18",
        "table": "eoutcome_18",
        "parent_id": "eOutcome",
        "type": "element",
    },
    {
        "id": "eOutcome.21",
        "table": "eoutcome_21",
        "parent_id": "eOutcome",
        "type": "element",
    },
]

EPATIENT_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {"id": "ePatient", "table": "epatient", "parent_id": None, "type": "group"},
    # Direct elements of ePatient
    {
        "id": "ePatient.01",
        "table": "epatient_01",
        "parent_id": "ePatient",
        "type": "element",
    },
    {
        "id": "ePatient.05",
        "table": "epatient_05",
        "parent_id": "ePatient",
        "type": "element",
    },
    {
        "id": "ePatient.06",
        "table": "epatient_06",
        "parent_id": "ePatient",
        "type": "element",
    },
    {
        "id": "ePatient.07",
        "table": "epatient_07",
        "parent_id": "ePatient",
        "type": "element",
    },
    {
        "id": "ePatient.08",
        "table": "epatient_08",
        "parent_id": "ePatient",
        "type": "element",
    },
    {
        "id": "ePatient.09",
        "table": "epatient_09",
        "parent_id": "ePatient",
        "type": "element",
    },
    {
        "id": "ePatient.10",
        "table": "epatient_10",
        "parent_id": "ePatient",
        "type": "element",
    },
    {
        "id": "ePatient.11",
        "table": "epatient_11",
        "parent_id": "ePatient",
        "type": "element",
    },
    {
        "id": "ePatient.12",
        "table": "epatient_12",
        "parent_id": "ePatient",
        "type": "element",
    },
    {
        "id": "ePatient.13",
        "table": "epatient_13",
        "parent_id": "ePatient",
        "type": "element",
    },
    {
        "id": "ePatient.14",
        "table": "epatient_14",
        "parent_id": "ePatient",
        "type": "element",
    },
    {
        "id": "ePatient.17",
        "table": "epatient_17",
        "parent_id": "ePatient",
        "type": "element",
    },
    {
        "id": "ePatient.18",
        "table": "epatient_18",
        "parent_id": "ePatient",
        "type": "element",
    },
    {
        "id": "ePatient.19",
        "table": "epatient_19",
        "parent_id": "ePatient",
        "type": "element",
    },
    {
        "id": "ePatient.20",
        "table": "epatient_20",
        "parent_id": "ePatient",
        "type": "element",
    },
    {
        "id": "ePatient.21",
        "table": "epatient_21",
        "parent_id": "ePatient",
        "type": "element",
    },
    {
        "id": "ePatient.22",
        "table": "epatient_22",
        "parent_id": "ePatient",
        "type": "element",
    },
    {
        "id": "ePatient.24",
        "table": "epatient_24",
        "parent_id": "ePatient",
        "type": "element",
    },
    {
        "id": "ePatient.25",
        "table": "epatient_25",
        "parent_id": "ePatient",
        "type": "element",
    },
    # PatientNameGroup
    {
        "id": "ePatient.PatientNameGroup",
        "table": "epatient_patientnamegroup",
        "parent_id": "ePatient",
        "type": "group",
    },
    {
        "id": "ePatient.02",
        "table": "epatient_02",
        "parent_id": "ePatient.PatientNameGroup",
        "type": "element",
    },
    {
        "id": "ePatient.03",
        "table": "epatient_03",
        "parent_id": "ePatient.PatientNameGroup",
        "type": "element",
    },
    {
        "id": "ePatient.04",
        "table": "epatient_04",
        "parent_id": "ePatient.PatientNameGroup",
        "type": "element",
    },
    {
        "id": "ePatient.23",
        "table": "epatient_23",
        "parent_id": "ePatient.PatientNameGroup",
        "type": "element",
    },
    # AgeGroup
    {
        "id": "ePatient.AgeGroup",
        "table": "epatient_agegroup",
        "parent_id": "ePatient",
        "type": "group",
    },
    {
        "id": "ePatient.15",
        "table": "epatient_15",
        "parent_id": "ePatient.AgeGroup",
        "type": "element",
    },
    {
        "id": "ePatient.16",
        "table": "epatient_16",
        "parent_id": "ePatient.AgeGroup",
        "type": "element",
    },
]

EPAYMENT_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {"id": "ePayment", "table": "epayment", "parent_id": None, "type": "group"},
    # Direct elements of ePayment
    {
        "id": "ePayment.01",
        "table": "epayment_01",
        "parent_id": "ePayment",
        "type": "element",
    },
    {
        "id": "ePayment.08",
        "table": "epayment_08",
        "parent_id": "ePayment",
        "type": "element",
    },
    {
        "id": "ePayment.40",
        "table": "epayment_40",
        "parent_id": "ePayment",
        "type": "element",
    },
    {
        "id": "ePayment.41",
        "table": "epayment_41",
        "parent_id": "ePayment",
        "type": "element",
    },
    {
        "id": "ePayment.42",
        "table": "epayment_42",
        "parent_id": "ePayment",
        "type": "element",
    },
    {
        "id": "ePayment.44",
        "table": "epayment_44",
        "parent_id": "ePayment",
        "type": "element",
    },
    {
        "id": "ePayment.45",
        "table": "epayment_45",
        "parent_id": "ePayment",
        "type": "element",
    },
    {
        "id": "ePayment.46",
        "table": "epayment_46",
        "parent_id": "ePayment",
        "type": "element",
    },
    {
        "id": "ePayment.47",
        "table": "epayment_47",
        "parent_id": "ePayment",
        "type": "element",
    },
    {
        "id": "ePayment.48",
        "table": "epayment_48",
        "parent_id": "ePayment",
        "type": "element",
    },
    {
        "id": "ePayment.49",
        "table": "epayment_49",
        "parent_id": "ePayment",
        "type": "element",
    },
    {
        "id": "ePayment.50",
        "table": "epayment_50",
        "parent_id": "ePayment",
        "type": "element",
    },
    {
        "id": "ePayment.51",
        "table": "epayment_51",
        "parent_id": "ePayment",
        "type": "element",
    },
    {
        "id": "ePayment.52",
        "table": "epayment_52",
        "parent_id": "ePayment",
        "type": "element",
    },
    {
        "id": "ePayment.53",
        "table": "epayment_53",
        "parent_id": "ePayment",
        "type": "element",
    },
    {
        "id": "ePayment.54",
        "table": "epayment_54",
        "parent_id": "ePayment",
        "type": "element",
    },
    {
        "id": "ePayment.57",
        "table": "epayment_57",
        "parent_id": "ePayment",
        "type": "element",
    },
    # CertificateGroup
    {
        "id": "ePayment.CertificateGroup",
        "table": "epayment_certificategroup",
        "parent_id": "ePayment",
        "type": "group",
    },
    {
        "id": "ePayment.02",
        "table": "epayment_02",
        "parent_id": "ePayment.CertificateGroup",
        "type": "element",
    },
    {
        "id": "ePayment.03",
        "table": "epayment_03",
        "parent_id": "ePayment.CertificateGroup",
        "type": "element",
    },
    {
        "id": "ePayment.04",
        "table": "epayment_04",
        "parent_id": "ePayment.CertificateGroup",
        "type": "element",
    },
    {
        "id": "ePayment.05",
        "table": "epayment_05",
        "parent_id": "ePayment.CertificateGroup",
        "type": "element",
    },
    {
        "id": "ePayment.06",
        "table": "epayment_06",
        "parent_id": "ePayment.CertificateGroup",
        "type": "element",
    },
    {
        "id": "ePayment.07",
        "table": "epayment_07",
        "parent_id": "ePayment.CertificateGroup",
        "type": "element",
    },
    # InsuranceGroup
    {
        "id": "ePayment.InsuranceGroup",
        "table": "epayment_insurancegroup",
        "parent_id": "ePayment",
        "type": "group",
    },
    {
        "id": "ePayment.09",
        "table": "epayment_09",
        "parent_id": "ePayment.InsuranceGroup",
        "type": "element",
    },
    {
        "id": "ePayment.10",
        "table": "epayment_10",
        "parent_id": "ePayment.InsuranceGroup",
        "type": "element",
    },
    {
        "id": "ePayment.11",
        "table": "epayment_11",
        "parent_id": "ePayment.InsuranceGroup",
        "type": "element",
    },
    {
        "id": "ePayment.12",
        "table": "epayment_12",
        "parent_id": "ePayment.InsuranceGroup",
        "type": "element",
    },
    {
        "id": "ePayment.13",
        "table": "epayment_13",
        "parent_id": "ePayment.InsuranceGroup",
        "type": "element",
    },
    {
        "id": "ePayment.14",
        "table": "epayment_14",
        "parent_id": "ePayment.InsuranceGroup",
        "type": "element",
    },
    {
        "id": "ePayment.15",
        "table": "epayment_15",
        "parent_id": "ePayment.InsuranceGroup",
        "type": "element",
    },
    {
        "id": "ePayment.16",
        "table": "epayment_16",
        "parent_id": "ePayment.InsuranceGroup",
        "type": "element",
    },
    {
        "id": "ePayment.17",
        "table": "epayment_17",
        "parent_id": "ePayment.InsuranceGroup",
        "type": "element",
    },
    {
        "id": "ePayment.18",
        "table": "epayment_18",
        "parent_id": "ePayment.InsuranceGroup",
        "type": "element",
    },
    {
        "id": "ePayment.19",
        "table": "epayment_19",
        "parent_id": "ePayment.InsuranceGroup",
        "type": "element",
    },
    {
        "id": "ePayment.20",
        "table": "epayment_20",
        "parent_id": "ePayment.InsuranceGroup",
        "type": "element",
    },
    {
        "id": "ePayment.21",
        "table": "epayment_21",
        "parent_id": "ePayment.InsuranceGroup",
        "type": "element",
    },
    {
        "id": "ePayment.22",
        "table": "epayment_22",
        "parent_id": "ePayment.InsuranceGroup",
        "type": "element",
    },
    {
        "id": "ePayment.58",
        "table": "epayment_58",
        "parent_id": "ePayment.InsuranceGroup",
        "type": "element",
    },
    {
        "id": "ePayment.59",
        "table": "epayment_59",
        "parent_id": "ePayment.InsuranceGroup",
        "type": "element",
    },
    {
        "id": "ePayment.60",
        "table": "epayment_60",
        "parent_id": "ePayment.InsuranceGroup",
        "type": "element",
    },
    # ClosestRelativeGroup
    {
        "id": "ePayment.ClosestRelativeGroup",
        "table": "epayment_closestrelativegroup",
        "parent_id": "ePayment",
        "type": "group",
    },
    {
        "id": "ePayment.23",
        "table": "epayment_23",
        "parent_id": "ePayment.ClosestRelativeGroup",
        "type": "element",
    },
    {
        "id": "ePayment.24",
        "table": "epayment_24",
        "parent_id": "ePayment.ClosestRelativeGroup",
        "type": "element",
    },
    {
        "id": "ePayment.25",
        "table": "epayment_25",
        "parent_id": "ePayment.ClosestRelativeGroup",
        "type": "element",
    },
    {
        "id": "ePayment.26",
        "table": "epayment_26",
        "parent_id": "ePayment.ClosestRelativeGroup",
        "type": "element",
    },
    {
        "id": "ePayment.27",
        "table": "epayment_27",
        "parent_id": "ePayment.ClosestRelativeGroup",
        "type": "element",
    },
    {
        "id": "ePayment.28",
        "table": "epayment_28",
        "parent_id": "ePayment.ClosestRelativeGroup",
        "type": "element",
    },
    {
        "id": "ePayment.29",
        "table": "epayment_29",
        "parent_id": "ePayment.ClosestRelativeGroup",
        "type": "element",
    },
    {
        "id": "ePayment.30",
        "table": "epayment_30",
        "parent_id": "ePayment.ClosestRelativeGroup",
        "type": "element",
    },
    {
        "id": "ePayment.31",
        "table": "epayment_31",
        "parent_id": "ePayment.ClosestRelativeGroup",
        "type": "element",
    },
    {
        "id": "ePayment.32",
        "table": "epayment_32",
        "parent_id": "ePayment.ClosestRelativeGroup",
        "type": "element",
    },
    # EmployerGroup
    {
        "id": "ePayment.EmployerGroup",
        "table": "epayment_employergroup",
        "parent_id": "ePayment",
        "type": "group",
    },
    {
        "id": "ePayment.33",
        "table": "epayment_33",
        "parent_id": "ePayment.EmployerGroup",
        "type": "element",
    },
    {
        "id": "ePayment.34",
        "table": "epayment_34",
        "parent_id": "ePayment.EmployerGroup",
        "type": "element",
    },
    {
        "id": "ePayment.35",
        "table": "epayment_35",
        "parent_id": "ePayment.EmployerGroup",
        "type": "element",
    },
    {
        "id": "ePayment.36",
        "table": "epayment_36",
        "parent_id": "ePayment.EmployerGroup",
        "type": "element",
    },
    {
        "id": "ePayment.37",
        "table": "epayment_37",
        "parent_id": "ePayment.EmployerGroup",
        "type": "element",
    },
    {
        "id": "ePayment.38",
        "table": "epayment_38",
        "parent_id": "ePayment.EmployerGroup",
        "type": "element",
    },
    {
        "id": "ePayment.39",
        "table": "epayment_39",
        "parent_id": "ePayment.EmployerGroup",
        "type": "element",
    },
    # SupplyItemGroup
    {
        "id": "ePayment.SupplyItemGroup",
        "table": "epayment_supplyitemgroup",
        "parent_id": "ePayment",
        "type": "group",
    },
    {
        "id": "ePayment.55",
        "table": "epayment_55",
        "parent_id": "ePayment.SupplyItemGroup",
        "type": "element",
    },
    {
        "id": "ePayment.56",
        "table": "epayment_56",
        "parent_id": "ePayment.SupplyItemGroup",
        "type": "element",
    },
]

EPROTOCOLS_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {"id": "eProtocols", "table": "eprotocols", "parent_id": None, "type": "group"},
    # ProtocolGroup
    {
        "id": "eProtocols.ProtocolGroup",
        "table": "eprotocols_protocolgroup",
        "parent_id": "eProtocols",
        "type": "group",
    },
    {
        "id": "eProtocols.01",
        "table": "eprotocols_01",
        "parent_id": "eProtocols.ProtocolGroup",
        "type": "element",
    },
    {
        "id": "eProtocols.02",
        "table": "eprotocols_02",
        "parent_id": "eProtocols.ProtocolGroup",
        "type": "element",
    },
]

ERECORD_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {"id": "eRecord", "table": "erecord", "parent_id": None, "type": "group"},
    # Direct element of eRecord
    {
        "id": "eRecord.01",
        "table": "erecord_01",
        "parent_id": "eRecord",
        "type": "element",
    },
    # SoftwareApplicationGroup
    {
        "id": "eRecord.SoftwareApplicationGroup",
        "table": "erecord_softwareapplicationgroup",
        "parent_id": "eRecord",
        "type": "group",
    },
    {
        "id": "eRecord.02",
        "table": "erecord_02",
        "parent_id": "eRecord.SoftwareApplicationGroup",
        "type": "element",
    },
    {
        "id": "eRecord.03",
        "table": "erecord_03",
        "parent_id": "eRecord.SoftwareApplicationGroup",
        "type": "element",
    },
    {
        "id": "eRecord.04",
        "table": "erecord_04",
        "parent_id": "eRecord.SoftwareApplicationGroup",
        "type": "element",
    },
]

ERESPONSE_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {"id": "eResponse", "table": "eresponse", "parent_id": None, "type": "group"},
    # AgencyGroup
    {
        "id": "eResponse.AgencyGroup",
        "table": "eresponse_agencygroup",
        "parent_id": "eResponse",
        "type": "group",
    },
    {
        "id": "eResponse.01",
        "table": "eresponse_01",
        "parent_id": "eResponse.AgencyGroup",
        "type": "element",
    },
    {
        "id": "eResponse.02",
        "table": "eresponse_02",
        "parent_id": "eResponse.AgencyGroup",
        "type": "element",
    },
    # Direct elements of eResponse
    {
        "id": "eResponse.03",
        "table": "eresponse_03",
        "parent_id": "eResponse",
        "type": "element",
    },
    {
        "id": "eResponse.04",
        "table": "eresponse_04",
        "parent_id": "eResponse",
        "type": "element",
    },
    # ServiceGroup
    {
        "id": "eResponse.ServiceGroup",
        "table": "eresponse_servicegroup",
        "parent_id": "eResponse",
        "type": "group",
    },
    {
        "id": "eResponse.05",
        "table": "eresponse_05",
        "parent_id": "eResponse.ServiceGroup",
        "type": "element",
    },
    {
        "id": "eResponse.06",
        "table": "eresponse_06",
        "parent_id": "eResponse.ServiceGroup",
        "type": "element",
    },
    # More direct elements of eResponse
    {
        "id": "eResponse.07",
        "table": "eresponse_07",
        "parent_id": "eResponse",
        "type": "element",
    },
    {
        "id": "eResponse.08",
        "table": "eresponse_08",
        "parent_id": "eResponse",
        "type": "element",
    },
    {
        "id": "eResponse.09",
        "table": "eresponse_09",
        "parent_id": "eResponse",
        "type": "element",
    },
    {
        "id": "eResponse.10",
        "table": "eresponse_10",
        "parent_id": "eResponse",
        "type": "element",
    },
    {
        "id": "eResponse.11",
        "table": "eresponse_11",
        "parent_id": "eResponse",
        "type": "element",
    },
    {
        "id": "eResponse.12",
        "table": "eresponse_12",
        "parent_id": "eResponse",
        "type": "element",
    },
    {
        "id": "eResponse.13",
        "table": "eresponse_13",
        "parent_id": "eResponse",
        "type": "element",
    },
    {
        "id": "eResponse.14",
        "table": "eresponse_14",
        "parent_id": "eResponse",
        "type": "element",
    },
    {
        "id": "eResponse.16",
        "table": "eresponse_16",
        "parent_id": "eResponse",
        "type": "element",
    },
    {
        "id": "eResponse.17",
        "table": "eresponse_17",
        "parent_id": "eResponse",
        "type": "element",
    },
    {
        "id": "eResponse.18",
        "table": "eresponse_18",
        "parent_id": "eResponse",
        "type": "element",
    },
    {
        "id": "eResponse.19",
        "table": "eresponse_19",
        "parent_id": "eResponse",
        "type": "element",
    },
    {
        "id": "eResponse.20",
        "table": "eresponse_20",
        "parent_id": "eResponse",
        "type": "element",
    },
    {
        "id": "eResponse.21",
        "table": "eresponse_21",
        "parent_id": "eResponse",
        "type": "element",
    },
    {
        "id": "eResponse.22",
        "table": "eresponse_22",
        "parent_id": "eResponse",
        "type": "element",
    },
    {
        "id": "eResponse.23",
        "table": "eresponse_23",
        "parent_id": "eResponse",
        "type": "element",
    },
    {
        "id": "eResponse.24",
        "table": "eresponse_24",
        "parent_id": "eResponse",
        "type": "element",
    },
]

ESCENE_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {"id": "eScene", "table": "escene", "parent_id": None, "type": "group"},
    # ResponderGroup
    {
        "id": "eScene.ResponderGroup",
        "table": "escene_respondergroup",
        "parent_id": "eScene",
        "type": "group",
    },
    {
        "id": "eScene.02",
        "table": "escene_02",
        "parent_id": "eScene.ResponderGroup",
        "type": "element",
    },
    {
        "id": "eScene.03",
        "table": "escene_03",
        "parent_id": "eScene.ResponderGroup",
        "type": "element",
    },
    {
        "id": "eScene.04",
        "table": "escene_04",
        "parent_id": "eScene.ResponderGroup",
        "type": "element",
    },
    {
        "id": "eScene.24",
        "table": "escene_24",
        "parent_id": "eScene.ResponderGroup",
        "type": "element",
    },
    {
        "id": "eScene.25",
        "table": "escene_25",
        "parent_id": "eScene.ResponderGroup",
        "type": "element",
    },
    # Direct elements of eScene
    {"id": "eScene.01", "table": "escene_01", "parent_id": "eScene", "type": "element"},
    {"id": "eScene.05", "table": "escene_05", "parent_id": "eScene", "type": "element"},
    {"id": "eScene.06", "table": "escene_06", "parent_id": "eScene", "type": "element"},
    {"id": "eScene.07", "table": "escene_07", "parent_id": "eScene", "type": "element"},
    {"id": "eScene.08", "table": "escene_08", "parent_id": "eScene", "type": "element"},
    {"id": "eScene.09", "table": "escene_09", "parent_id": "eScene", "type": "element"},
    {"id": "eScene.10", "table": "escene_10", "parent_id": "eScene", "type": "element"},
    {"id": "eScene.11", "table": "escene_11", "parent_id": "eScene", "type": "element"},
    {"id": "eScene.12", "table": "escene_12", "parent_id": "eScene", "type": "element"},
    {"id": "eScene.13", "table": "escene_13", "parent_id": "eScene", "type": "element"},
    {"id": "eScene.14", "table": "escene_14", "parent_id": "eScene", "type": "element"},
    {"id": "eScene.15", "table": "escene_15", "parent_id": "eScene", "type": "element"},
    {"id": "eScene.16", "table": "escene_16", "parent_id": "eScene", "type": "element"},
    {"id": "eScene.17", "table": "escene_17", "parent_id": "eScene", "type": "element"},
    {"id": "eScene.18", "table": "escene_18", "parent_id": "eScene", "type": "element"},
    {"id": "eScene.19", "table": "escene_19", "parent_id": "eScene", "type": "element"},
    {"id": "eScene.20", "table": "escene_20", "parent_id": "eScene", "type": "element"},
    {"id": "eScene.21", "table": "escene_21", "parent_id": "eScene", "type": "element"},
    {"id": "eScene.22", "table": "escene_22", "parent_id": "eScene", "type": "element"},
    {"id": "eScene.23", "table": "escene_23", "parent_id": "eScene", "type": "element"},
]

ESITUATION_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {"id": "eSituation", "table": "esituation", "parent_id": None, "type": "group"},
    # Direct elements of eSituation
    {
        "id": "eSituation.01",
        "table": "esituation_01",
        "parent_id": "eSituation",
        "type": "element",
    },
    {
        "id": "eSituation.02",
        "table": "esituation_02",
        "parent_id": "eSituation",
        "type": "element",
    },
    # PatientComplaintGroup
    {
        "id": "eSituation.PatientComplaintGroup",
        "table": "esituation_patientcomplaintgroup",
        "parent_id": "eSituation",
        "type": "group",
    },
    {
        "id": "eSituation.03",
        "table": "esituation_03",
        "parent_id": "eSituation.PatientComplaintGroup",
        "type": "element",
    },
    {
        "id": "eSituation.04",
        "table": "esituation_04",
        "parent_id": "eSituation.PatientComplaintGroup",
        "type": "element",
    },
    {
        "id": "eSituation.05",
        "table": "esituation_05",
        "parent_id": "eSituation.PatientComplaintGroup",
        "type": "element",
    },
    {
        "id": "eSituation.06",
        "table": "esituation_06",
        "parent_id": "eSituation.PatientComplaintGroup",
        "type": "element",
    },
    # More direct elements of eSituation
    {
        "id": "eSituation.07",
        "table": "esituation_07",
        "parent_id": "eSituation",
        "type": "element",
    },
    {
        "id": "eSituation.08",
        "table": "esituation_08",
        "parent_id": "eSituation",
        "type": "element",
    },
    {
        "id": "eSituation.09",
        "table": "esituation_09",
        "parent_id": "eSituation",
        "type": "element",
    },
    {
        "id": "eSituation.10",
        "table": "esituation_10",
        "parent_id": "eSituation",
        "type": "element",
    },
    {
        "id": "eSituation.11",
        "table": "esituation_11",
        "parent_id": "eSituation",
        "type": "element",
    },
    {
        "id": "eSituation.12",
        "table": "esituation_12",
        "parent_id": "eSituation",
        "type": "element",
    },
    {
        "id": "eSituation.13",
        "table": "esituation_13",
        "parent_id": "eSituation",
        "type": "element",
    },
    # WorkRelatedGroup
    {
        "id": "eSituation.WorkRelatedGroup",
        "table": "esituation_workrelatedgroup",
        "parent_id": "eSituation",
        "type": "group",
    },
    {
        "id": "eSituation.14",
        "table": "esituation_14",
        "parent_id": "eSituation.WorkRelatedGroup",
        "type": "element",
    },
    {
        "id": "eSituation.15",
        "table": "esituation_15",
        "parent_id": "eSituation.WorkRelatedGroup",
        "type": "element",
    },
    {
        "id": "eSituation.16",
        "table": "esituation_16",
        "parent_id": "eSituation.WorkRelatedGroup",
        "type": "element",
    },
    # More direct elements of eSituation
    {
        "id": "eSituation.17",
        "table": "esituation_17",
        "parent_id": "eSituation",
        "type": "element",
    },
    {
        "id": "eSituation.18",
        "table": "esituation_18",
        "parent_id": "eSituation",
        "type": "element",
    },
    {
        "id": "eSituation.19",
        "table": "esituation_19",
        "parent_id": "eSituation",
        "type": "element",
    },
    {
        "id": "eSituation.20",
        "table": "esituation_20",
        "parent_id": "eSituation",
        "type": "element",
    },
]

ETIMES_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {
        "id": "eTimes",
        "table": "etimes",
        "parent_id": None,
        "type": "group",
    },
    # Direct Children of eTimes
    {
        "id": "eTimes.01",
        "table": "etimes_01",
        "parent_id": "eTimes",
        "type": "element",
    },
    {
        "id": "eTimes.02",
        "table": "etimes_02",
        "parent_id": "eTimes",
        "type": "element",
    },
    {
        "id": "eTimes.03",
        "table": "etimes_03",
        "parent_id": "eTimes",
        "type": "element",
    },
    {
        "id": "eTimes.04",
        "table": "etimes_04",
        "parent_id": "eTimes",
        "type": "element",
    },
    {
        "id": "eTimes.05",
        "table": "etimes_05",
        "parent_id": "eTimes",
        "type": "element",
    },
    {
        "id": "eTimes.06",
        "table": "etimes_06",
        "parent_id": "eTimes",
        "type": "element",
    },
    {
        "id": "eTimes.07",
        "table": "etimes_07",
        "parent_id": "eTimes",
        "type": "element",
    },
    {
        "id": "eTimes.08",
        "table": "etimes_08",
        "parent_id": "eTimes",
        "type": "element",
    },
    {
        "id": "eTimes.09",
        "table": "etimes_09",
        "parent_id": "eTimes",
        "type": "element",
    },
    {
        "id": "eTimes.10",
        "table": "etimes_10",
        "parent_id": "eTimes",
        "type": "element",
    },
    {
        "id": "eTimes.11",
        "table": "etimes_11",
        "parent_id": "eTimes",
        "type": "element",
    },
    {
        "id": "eTimes.12",
        "table": "etimes_12",
        "parent_id": "eTimes",
        "type": "element",
    },
    {
        "id": "eTimes.13",
        "table": "etimes_13",
        "parent_id": "eTimes",
        "type": "element",
    },
    {
        "id": "eTimes.14",
        "table": "etimes_14",
        "parent_id": "eTimes",
        "type": "element",
    },
    {
        "id": "eTimes.15",
        "table": "etimes_15",
        "parent_id": "eTimes",
        "type": "element",
    },
    {
        "id": "eTimes.16",
        "table": "etimes_16",
        "parent_id": "eTimes",
        "type": "element",
    },
    {
        "id": "eTimes.17",
        "table": "etimes_17",
        "parent_id": "eTimes",
        "type": "element",
    },
]

ECUSTOMCONFIGURATION_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {
        "id": "eCustomConfiguration",
        "table": "ecustomconfiguration",
        "parent_id": None,
        "type": "group",
    },
    # CustomGroup
    {
        "id": "eCustomConfiguration.CustomGroup",
        "table": "ecustomconfiguration_customgroup",
        "parent_id": "eCustomConfiguration",
        "type": "group",
    },
    {
        "id": "eCustomConfiguration.01",
        "table": "ecustomconfiguration_01",
        "parent_id": "eCustomConfiguration.CustomGroup",
        "type": "element",
    },
    {
        "id": "eCustomConfiguration.02",
        "table": "ecustomconfiguration_02",
        "parent_id": "eCustomConfiguration.CustomGroup",
        "type": "element",
    },
    {
        "id": "eCustomConfiguration.03",
        "table": "ecustomconfiguration_03",
        "parent_id": "eCustomConfiguration.CustomGroup",
        "type": "element",
    },
    {
        "id": "eCustomConfiguration.04",
        "table": "ecustomconfiguration_04",
        "parent_id": "eCustomConfiguration.CustomGroup",
        "type": "element",
    },
    {
        "id": "eCustomConfiguration.05",
        "table": "ecustomconfiguration_05",
        "parent_id": "eCustomConfiguration.CustomGroup",
        "type": "element",
    },
    {
        "id": "eCustomConfiguration.06",
        "table": "ecustomconfiguration_06",
        "parent_id": "eCustomConfiguration.CustomGroup",
        "type": "element",
    },
    {
        "id": "eCustomConfiguration.07",
        "table": "ecustomconfiguration_07",
        "parent_id": "eCustomConfiguration.CustomGroup",
        "type": "element",
    },
    {
        "id": "eCustomConfiguration.08",
        "table": "ecustomconfiguration_08",
        "parent_id": "eCustomConfiguration.CustomGroup",
        "type": "element",
    },
    {
        "id": "eCustomConfiguration.09",
        "table": "ecustomconfiguration_09",
        "parent_id": "eCustomConfiguration.CustomGroup",
        "type": "element",
    },
]

ECUSTOMRESULTS_STRUCTURE = [
    # Base Group (Parent of all direct children)
    {
        "id": "eCustomResults",
        "table": "ecustomresults",
        "parent_id": None,
        "type": "group",
    },
    # ResultsGroup
    {
        "id": "eCustomResults.ResultsGroup",
        "table": "ecustomresults_resultsgroup",
        "parent_id": "eCustomResults",
        "type": "group",
    },
    {
        "id": "eCustomResults.01",
        "table": "ecustomresults_01",
        "parent_id": "eCustomResults.ResultsGroup",
        "type": "element",
    },
    {
        "id": "eCustomResults.02",
        "table": "ecustomresults_02",
        "parent_id": "eCustomResults.ResultsGroup",
        "type": "element",
    },
    {
        "id": "eCustomResults.03",
        "table": "ecustomresults_03",
        "parent_id": "eCustomResults.ResultsGroup",
        "type": "element",
    },
]
