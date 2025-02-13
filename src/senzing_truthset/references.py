"""TruthSet data for REFERENCES"""

from typing import Any, Dict

TRUTHSET_REFERENCE_RECORDS: Dict[Any, Any] = {
    "2012": {
        "DataSource": "REFERENCE",
        "Id": "2012",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2012", "RECORD_TYPE": "ORGANIZATION", "PRIMARY_NAME_ORG": "Hajah Maimunah", "ADDR_TYPE": "REGISTERED", "ADDR_LINE1": "4 Hillview Rise", "ADDR_CITY": "SINGAPORE", "ADDR_POSTAL_CODE": "667979", "ADDR_COUNTRY": "Singapore", "REL_ANCHOR_KEY": "2011", "DATE": "2010", "STATUS": "Active", "CATEGORY": "Proprietorship"}',
    },
    "2013": {
        "DataSource": "REFERENCE",
        "Id": "2013",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2013", "RECORD_TYPE": "PERSON", "PRIMARY_NAME_FULL": "Wang Jie", "DATE_OF_BIRTH": "1993-09-14", "REL_POINTER_KEY": "2011", "REL_POINTER_ROLE": "Owns 60%", "STATUS": "Current", "CATEGORY": "Owner"}',
    },
    "2014": {
        "DataSource": "REFERENCE",
        "Id": "2014",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2014", "RECORD_TYPE": "PERSON", "PRIMARY_NAME_FULL": "Wang Wei", "DATE_OF_BIRTH": "1997-09-14", "REL_POINTER_KEY": "2011", "REL_POINTER_ROLE": "Owns 40%", "STATUS": "Current", "CATEGORY": "Owner"}',
    },
    "2041": {
        "DataSource": "REFERENCE",
        "Id": "2041",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2041", "RECORD_TYPE": "ORGANIZATION", "PRIMARY_NAME_ORG": "M\u00fcllenkranz ", "SECONDARY_NAME_ORG": "Autowerkz", "ADDR_TYPE": "PRIMARY", "ADDR_LINE1": "Hardenbergstra\u00dfe 87", "ADDR_CITY": "Rheinland-Pfalz", "ADDR_POSTAL_CODE": "66879", "ADDR_COUNTRY": "Germany", "REL_ANCHOR_KEY": "2041", "DATE": "2009", "STATUS": "Inactive", "CATEGORY": "Partnership"}',
    },
    "2051": {
        "DataSource": "REFERENCE",
        "Id": "2051",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2051", "RECORD_TYPE": "PERSON", "EMPLOYER_NAME": "M\u00fcllenkranz", "PRIMARY_NAME_FULL": "Faisal Siddiqui", "ADDR_TYPE": "HOME", "ADDR_LINE1": "Jia Musa Shahdara Sheikhupura Road", "ADDR_CITY": "Lahore", "ADDR_COUNTRY": "Pakistan", "PHONE_NUMBER": "+92 42-7925774", "REL_POINTER_KEY": "2041", "REL_POINTER_ROLE": "President", "STATUS": "Current", "CATEGORY": "President"}',
    },
    "2061": {
        "DataSource": "REFERENCE",
        "Id": "2061",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2061", "RECORD_TYPE": "PERSON", "EMPLOYER_NAME": "M\u00fcllenkranz", "NATIVE_NAME_FULL": "\u0412\u0410\u0421\u0406\u041b\u042c\u0415\u040e, \u0410\u043b\u044f\u043a\u0441\u0430\u043d\u0434\u0440 \u041f\u0430\u045e\u043b\u0430\u0432\u0456\u0447", "ADDR_FULL": "Tolmacheva Ul., bld. 8, appt. 71 Smolensk", "ADDR_COUNTRY": "RUS", "PHONE_TYPE": "PRIMARY", "PHONE_NUMBER": "+7(4812)85-62-34", "REL_POINTER_KEY": "2041", "REL_POINTER_ROLE": "Owns 100%", "STATUS": "Current", "CATEGORY": "Owner"}',
    },
    "2071": {
        "DataSource": "REFERENCE",
        "Id": "2071",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2071", "RECORD_TYPE": "ORGANIZATION", "PRIMARY_NAME_ORG": "Universal Exports, USA", "SECONDARY_NAME_ORG": "Universal Exports", "ADDR_TYPE": "BUSINESS", "ADDR_FULL": "Hughes Plaza, 100 Howard Hughes Way, Las Vegas, NV 89111", "PHONE_NUMBER": "800-111-1234", "REL_ANCHOR_KEY": "2071", "REL_POINTER_KEY": "2074", "REL_POINTER_ROLE": "Global Parent", "DATE": "1990", "STATUS": "Active", "CATEGORY": "Corporation"}',
    },
    "2074": {
        "DataSource": "REFERENCE",
        "Id": "2074",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2074", "RECORD_TYPE": "ORGANIZATION", "PRIMARY_NAME_ORG": "Universal Exports Worldwide", "SECONDARY_NAME_ORG": "Universal Exports", "ADDR_TYPE": "REGISTERED", "ADDR_LINE1": "405 Lexington Avenue", "ADDR_CITY": "Manhattan", "ADDR_STATE": "NY", "ADDR_POSTAL_CODE": "10174", "REL_ANCHOR_KEY": "2074", "DATE": "1990", "STATUS": "Active", "CATEGORY": "Corporation"}',
    },
    "2081": {
        "DataSource": "REFERENCE",
        "Id": "2081",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2081", "RECORD_TYPE": "PERSON", "EMPLOYER_NAME": "Universal Exports Worldwide", "PRIMARY_NAME_FULL": "Howard Hughess", "REL_POINTER_KEY": "2074", "REL_POINTER_ROLE": "Owns 50%", "STATUS": "Current", "CATEGORY": "Owner"}',
    },
    "2091": {
        "DataSource": "REFERENCE",
        "Id": "2091",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2091", "RECORD_TYPE": "PERSON", "EMPLOYER_NAME": "Universal Exports Worldwide", "PRIMARY_NAME_FULL": "Margaret Charney", "REL_POINTER_KEY": "2074", "REL_POINTER_ROLE": "Owns 50%", "STATUS": "Current", "CATEGORY": "Owner"}',
    },
    "2101": {
        "DataSource": "REFERENCE",
        "Id": "2101",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2101", "RECORD_TYPE": "PERSON", "EMPLOYER_NAME": "Universal Exports, USA", "PRIMARY_NAME_FULL": "Keeley Jones", "PHONE_NUMBER": "818-892-2818", "EMAIL_ADDRESS": "kjones@universal.com", "REL_POINTER_KEY": "2071", "REL_POINTER_ROLE": "Principal", "STATUS": "Current", "CATEGORY": "Director"}',
    },
    "2102": {
        "DataSource": "REFERENCE",
        "Id": "2102",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2102", "RECORD_TYPE": "PERSON", "PRIMARY_NAME_FULL": "Jones, Kaylee", "PHONE_NUMBER": "18188922818", "EMAIL_ADDRESS": "kjones@universal.com", "STATUS": "Active", "CATEGORY": "Contact"}',
    },
    "2111": {
        "DataSource": "REFERENCE",
        "Id": "2111",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2111", "RECORD_TYPE": "PERSON", "EMPLOYER_NAME": "Universal Exports, USA", "PRIMARY_NAME_FULL": "Susan Meyer", "ADDR_TYPE": "PRIMARY", "ADDR_LINE1": "Fieldstrasse 10, FL-2198 Triesen", "ADDR_COUNTRY": "Lichtenstein", "REL_POINTER_KEY": "2071", "REL_POINTER_ROLE": "Principal", "STATUS": "Current", "CATEGORY": "Director"}',
    },
    "2112": {
        "DataSource": "REFERENCE",
        "Id": "2112",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2112", "RECORD_TYPE": "PERSON", "PRIMARY_NAME_FULL": "Susan Meyer Thomas", "ADDR_TYPE": "PRIMARY", "ADDR_FULL": "Fieldstrasse 10, FL-2198 Triesen, Lichtenstein", "STATUS": "Active", "CATEGORY": "Contact"}',
    },
    "2121": {
        "DataSource": "REFERENCE",
        "Id": "2121",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2121", "RECORD_TYPE": "PERSON", "EMPLOYER_NAME": "Universal Exports, USA", "PRIMARY_NAME_FULL": "Kristen Salinger", "ADDR_TYPE": "PRIMARY", "ADDR_LINE1": "123 King street", "ADDR_CITY": "New York", "ADDR_STATE": "NY", "ADDR_POSTAL_CODE": "10012", "PHONE_TYPE": "MOBILE", "PHONE_NUMBER": "320-392-2137", "REL_POINTER_KEY": "2071", "REL_POINTER_ROLE": "Principal", "STATUS": "Current", "CATEGORY": "Director"}',
    },
    "2122": {
        "DataSource": "REFERENCE",
        "Id": "2122",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2122", "RECORD_TYPE": "PERSON", "PRIMARY_NAME_FULL": "Salenger, Kristin", "ADDR_TYPE": "PRIMARY", "ADDR_LINE1": "8321 Duke Street", "ADDR_CITY": "Los Angeles", "ADDR_STATE": "CA", "ADDR_POSTAL_CODE": "90015", "PHONE_TYPE": "MOBILE", "PHONE_NUMBER": "(320) 392-2137", "STATUS": "Active", "CATEGORY": "Contact"}',
    },
    "2131": {
        "DataSource": "REFERENCE",
        "Id": "2131",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2131", "RECORD_TYPE": "PERSON", "EMPLOYER_NAME": "Universal Exports, USA", "PRIMARY_NAME_FULL": "Rosemay A Thomas", "ADDR_TYPE": "PRIMARY", "ADDR_FULL": "18 Danver Place, Loughborough, Leicestershire, LE11 1UU, United Kingdom", "REL_POINTER_KEY": "2071", "REL_POINTER_ROLE": "Principal", "STATUS": "Current", "CATEGORY": "Director"}',
    },
    "2132": {
        "DataSource": "REFERENCE",
        "Id": "2132",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2132", "RECORD_TYPE": "PERSON", "PRIMARY_NAME_LAST": "Thomas", "PRIMARY_NAME_FIRST": "Rosemary A", "ADDR_TYPE": "PRIMARY", "ADDR_FULL": "18 Danver Place, Loughborough, Leicestershire, United Kingdom, LE11 1UU", "STATUS": "Active", "CATEGORY": "Contact"}',
    },
    "2141": {
        "DataSource": "REFERENCE",
        "Id": "2141",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2141", "RECORD_TYPE": "ORGANIZATION", "PRIMARY_NAME_ORG": "Universal Exports Singapore", "SECONDARY_NAME_ORG": "Universal Exports", "ADDR_TYPE": "REGISTERED", "ADDR_FULL": "Chinatown Point, 133 New Bridge Road, 059413 singapore", "ADDR_COUNTRY": "Singapore", "REL_POINTER_KEY": "2074", "REL_POINTER_ROLE": "Global Parent", "DATE": "1994", "STATUS": "Active", "CATEGORY": "Corporation"}',
    },
    "2151": {
        "DataSource": "REFERENCE",
        "Id": "2151",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2151", "RECORD_TYPE": "ORGANIZATION", "PRIMARY_NAME_ORG": "Universal Exports India", "SECONDARY_NAME_ORG": "Universal Exports", "ADDR_TYPE": "REGISTERED", "ADDR_FULL": "Mullanpara Road, Vythiri, 673576, India", "REL_POINTER_KEY": "2074", "REL_POINTER_ROLE": "Global Parent", "DATE": "1998", "STATUS": "Active", "CATEGORY": "Corporation"}',
    },
    "2161": {
        "DataSource": "REFERENCE",
        "Id": "2161",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2161", "RECORD_TYPE": "PERSON", "EMPLOYER_NAME": "Universal Exports, USA", "PRIMARY_NAME_LAST": "Alexopoulos", "PRIMARY_NAME_FIRST": "Anastassia", "ADDR_TYPE": "HOME", "ADDR_LINE1": "6781 Metaxa Forest, Suite 296", "ADDR_CITY": "Athens", "ADDR_STATE": "GA", "ADDR_POSTAL_CODE": "30009", "EMAIL_ADDRESS": "Nastassia<patak@universal.com>", "REL_POINTER_KEY": "2071", "REL_POINTER_ROLE": "Principal", "STATUS": "Current", "CATEGORY": "Director"}',
    },
    "2162": {
        "DataSource": "REFERENCE",
        "Id": "2162",
        "Json": '{"DATA_SOURCE": "REFERENCE", "RECORD_ID": "2162", "RECORD_TYPE": "PERSON", "PRIMARY_NAME_FULL": "Alexopoulos, Nastassia", "ADDR_TYPE": "PRIMARY", "ADDR_LINE1": "6781 Metaxa Forest", "ADDR_CITY": "Athens", "ADDR_STATE": "GA", "ADDR_POSTAL_CODE": "30009", "EMAIL_ADDRESS": "patak@universal.com", "STATUS": "Active", "CATEGORY": "Contact"}',
    },
}
