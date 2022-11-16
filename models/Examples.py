class Examples:
    qbody_response_example = {
        "res": [
            {
                "q0": [
                    {
                        "id": "1",
                        "log_msg": "test log"
                    },
                    {
                        "id": "2",
                        "log_msg": "test log"
                    }
                ]
            },
            {
                "q1": [
                    {
                        "id": "1",
                        "msg": "123",
                        "ts": "2022-11-15 19:45:12"
                    }
                ]
            }
        ]
    }

    qbody_request_example = { 
        'db': 'dct_mysql01', 
        'q': 'select * from `events`;' 
    }