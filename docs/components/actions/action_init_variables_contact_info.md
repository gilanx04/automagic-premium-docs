---
title: "Action - Init Variables Contact Info"
source: https://automagic4android.com/action_init_variables_contact_info_en.html
archived: 2024-04-20
archive_url: https://web.archive.org/web/20240420131343/https://automagic4android.com/action_init_variables_contact_info_en.html
category: action
---

# Action - Init Variables Contact Info

The action **Init Variables Contact Info** loads information of the specified contact and stores the information in a map.

Tip: Condition **Debug Dialog** can be used to display the keys and values stored in the map.

Examples:

- Show all phone numbers of a contact.

Example JSON of a contact:
```
        {
          "display_name": "Contact XYZ", // name of the contact
          "photo_thumb_uri": "content://com.android.contacts/contacts/124/photo", // URI of the small image
          "photo_uri": "content://com.android.contacts/display_photo/3", // URI of the larger image
          "last_time_contacted": 1479667934531, // point in time of the last contact, 0 when not known
          "starred": true, // whether the contact is in the favorites or not
          "times_contacted": 1, // count of contacts (according to contact app)
          "phone_list": [{ // list of phone numbers
            "number": "+41987654321",
            "type": 2,
            "type_label": "Mobile"
          }, ... ],
          "organization_list": [{ // list of organizations
            "company": "Company X",
            "type": 2,
            "type_label": "Other",
            "title": "Company"
          }, ... ],
          "note_list": [{ // list of notes
              "note": "Note 1"
            }, ... ],
          "nickname_list": [{ // list of nicknames
            "nickname": "MR. incredible",
            "type": 0,
            "type_label": "Other"
          }, ... ],
          "email_list": [{ // list of email addresses
            "email": "example@gmail.com",
            "type": 1,
            "type_label": "Home"
          }, ... ],
          "relation_list": [{ // list of relations
            "relation": "Person 123",
            "type": 1,
            "type_label": "Assistant
          }, ... ],
          "structured_postal_list": [{ // list of addresses
            "formatted_address": "Mainstreet X\n1234 City",
            "type": 1,
            "type_label": "Home",
            "street": "Mainstreet X",
            "city": "City",
            "postcode": "1234"
          }, ... ],
          "structured_name_list": [{ // list of the names
            "display_name": "Contact XYZ",
            "given_name": "Contact",
            "family_name": "XYZ"
          }, ... ],
          "website_list": [{ // list of websites
            "url": "www.automagic4android.com",
            "type": 7,
            "type_label": "Other"
          }, ... ],
          "sip_address_list": [{ // list of the SIP addresses
            "number": "+41987654321",
            "type": 2,
            "type_label": "Mobile"
          }, ... ],
          "event_list": [{ // list of events
            "start_date": "1978-07-04",
            "type": 3,
            "type_label": "Birthday"
          }, ...],
          "group_list": [ // list of the groups
            "Group1",
            "Group2",
            "Group3"
          ]
        }
```

Please note that additional key value pairs might be added in future versions of Automagic.

Examples of access to values in action **Script**:
```
        name = contact_info["display_name"];
        photo_uri = contact_info["photo_uri"];
        phone1 = contact_info["phone_list"][0]["number"];
        phone2 = contact_info["phone_list"][1]["number"];
        phone2type = contact_info["phone_list"][1]["type_label"];
        nickname1 = contact_info["nickname_list"][0]["nickname"];
```

### Settings

#### Search type

Defines how the contact should be searched. The first found contact is used to provide the information.

#### Search value

The value used to search the contact. [Variables are supported.](action_script.md#string-inline-expressions)

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `contact_info` — the map containing the queried information

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
