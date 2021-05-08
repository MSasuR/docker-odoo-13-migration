# Copyright 2021 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.delete_records_safely_by_xml_id(
        env, [
            "l10n_fr.tag_fr_01",
            "l10n_fr.tag_fr_02",
            "l10n_fr.tag_fr_03",
            "l10n_fr.tag_fr_04",
            "l10n_fr.tag_fr_05",
            "l10n_fr.tag_fr_06",
            "l10n_fr.tag_fr_07",
            "l10n_fr.tag_fr_08",
            "l10n_fr.tag_fr_09",
            "l10n_fr.tag_fr_10",
            "l10n_fr.tag_fr_11",
            "l10n_fr.tag_fr_12",
            "l10n_fr.tag_fr_13",
            "l10n_fr.tag_fr_14",
            "l10n_fr.tag_fr_15",
            "l10n_fr.tag_fr_16",
            "l10n_fr.tag_fr_17",
            "l10n_fr.tag_fr_18",
            "l10n_fr.tag_fr_19",
            "l10n_fr.tag_fr_20",
            "l10n_fr.tag_fr_22",
            "l10n_fr.tag_fr_23",
            "l10n_fr.tag_fr_24",
            "l10n_fr.tag_fr_25",
            "l10n_fr.tag_fr_26",
            "l10n_fr.tag_fr_27",
            "l10n_fr.tag_fr_28",
            "l10n_fr.tag_fr_29",
            "l10n_fr.tag_fr_30",
            "l10n_fr.tag_fr_31",
            "l10n_fr.tag_fr_32",
            "l10n_fr.tag_fr_33",
            "l10n_fr.tag_fr_34",
            "l10n_fr.tag_fr_35",
            "l10n_fr.tag_fr_36",
            "l10n_fr.tag_fr_37",
            "l10n_fr.tag_fr_38",
            "l10n_fr.tag_fr_39",
            "l10n_fr.tag_fr_40",
            "l10n_fr.tag_fr_41",
            "l10n_fr.tag_fr_42",
            "l10n_fr.tag_fr_43",
            "l10n_fr.tag_fr_44",
            "l10n_fr.tag_fr_45",
            "l10n_fr.tag_fr_46",
            "l10n_fr.tag_fr_47",
            "l10n_fr.tag_fr_48",
            "l10n_fr.tag_fr_49",
            "l10n_fr.tag_fr_50",
            "l10n_fr.tag_fr_51",
            "l10n_fr.tag_fr_52",
            "l10n_fr.tag_fr_53",
            "l10n_fr.tag_fr_54",
            "l10n_fr.tag_fr_55",
            "l10n_fr.tag_fr_56",
            "l10n_fr.tag_fr_57",
            "l10n_fr.tag_fr_58",
            "l10n_fr.tag_fr_59",
            "l10n_fr.tag_fr_60",
            "l10n_fr.tag_fr_61",
            "l10n_fr.tag_fr_62",
            "l10n_fr.tag_fr_63",
            "l10n_fr.tag_fr_64",
            "l10n_fr.tag_fr_65",
            "l10n_fr.tag_fr_66",
            "l10n_fr.tag_fr_67",
            "l10n_fr.tag_fr_68",
            "l10n_fr.tag_fr_69",
            "l10n_fr.tag_fr_70",
            "l10n_fr.tag_fr_71",
            "l10n_fr.tag_fr_72",
            "l10n_fr.tag_fr_73",
            "l10n_fr.tag_fr_74",
            "l10n_fr.tag_fr_75",
            "l10n_fr.tag_fr_76",
            "l10n_fr.tag_fr_77",
            "l10n_fr.tag_fr_78",
            "l10n_fr.tag_fr_79",
            "l10n_fr.tag_fr_80",
            "l10n_fr.tag_fr_81",
            "l10n_fr.tag_fr_82",
            "l10n_fr.tag_fr_83",
            "l10n_fr.tag_fr_84",
            "l10n_fr.tag_fr_85",
            "l10n_fr.tag_fr_86",
            "l10n_fr.tag_fr_87",
            "l10n_fr.tag_fr_88",
            "l10n_fr.tag_fr_89",
            "l10n_fr.tag_fr_90",
            "l10n_fr.tag_fr_91",
            "l10n_fr.tag_fr_92",
            "l10n_fr.tag_fr_93",
            "l10n_fr.tag_fr_94",
            "l10n_fr.tag_fr_95",
            "l10n_fr.tag_fr_96",
            "l10n_fr.tag_fr_97",
        ]
    )