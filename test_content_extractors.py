from content_extractors import extract_values_and_styles


def test_extract_values_and_styles():
    data = {
        "nodeType": "document",
        "content": [
            {
                "nodeType": "paragraph",
                "content": [
                    {
                        "nodeType": "text",
                        "value": "This is some text.",
                        "marks": [{"type": "bold"}],
                    },
                    {
                        "nodeType": "hyperlink",
                        "content": [
                            {
                                "nodeType": "text",
                                "value": "This is a link.",
                                "marks": [],
                            }
                        ],
                        "data": {"uri": "https://example.com"},
                    },
                ],
            }
        ],
    }

    expected_result = [
        {"type": "text", "value": "This is some text.", "marks": [{"type": "bold"}]},
        {
            "type": "hyperlink",
            "value": "This is a link.",
            "uri": "https://example.com",
            "marks": [],
        },
    ]

    assert extract_values_and_styles(data) == expected_result
