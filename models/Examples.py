class Examples:
    qbody_responses = {
        200: {
            "content": {
                "application/json": {
                    "example": {
                        "res": "OK",
                        "data": [
                            {
                                "q0": [
                                    {
                                        "id": "1",
                                        "msg": "123",
                                        "ts": "2022-11-15 19:45:12"
                                    }
                                ]
                            },
                            {
                                "q1": [
                                    {
                                        "id": "1",
                                        "log_msg": "test log"
                                    },
                                    {
                                        "id": "2",
                                        "log_msg": "test log"
                                    }
                                ]
                            }
                        ],
                        "err": ""
                    }
                }
            },
        },
        500: {
            "content": {
                "application/json": {
                    "example": {
                        "res": "NOK",
                        "data": [],
                        "err": "1146 (42S02): Table 'dct_mysql01.2events' doesn't exist"
                    }
                }
            },
        },
    }

    qbody_request_example = { 
        'db': 'dct_mysql01', 
        'q': 'select * from `events`;' 
    }