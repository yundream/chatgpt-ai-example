import openai
import json

openai.api_key = "<<Your OpenAI API KEY>>" 
message= [{"role": "user", "content": "월요일 오사카행 비행기를 예약 하려 합니다. 출발지는 인천입니다."}]

def reservation_airplane(reservation_info):
    departure_date = reservation_info['day']
    departure_point = reservation_info['departure_point']
    destination_point = reservation_info['destination']
    transportation_type = reservation_info['transportation']
    print( f"예약 정보 >> {departure_date}: {departure_point} 출발 {destination_point} 행 {transportation_type}")
    print( f"""SELECT * FROM reservation_table 
          WHERE departure_date = '{departure_date}' 
          AND departure_point = '{departure_point}' 
          AND destination_point = '{destination_point}' 
          AND transportation_type = '{transportation_type}'""")
          # 실제 DB 쿼리는 생략 했습니다.
    return json_reponse

completion = openai.chat.completions.create(
    model="gpt-3.5-turbo-0613",
    messages=message,
    functions=[{
        "name": "reservation_airplane",
        "function_call":"auto",
        "parameters": {
            "type": "object",
            "properties": {
                "day": {
                    "type": "string",
                    "description": "Day of the week. For example Monday, Tuesday, etc."
                },
                "departure_point": {
                    "type": "string",
                    "description": "starting point of the travel"
                },
                "destination": {
                    "type": "string",
                    "description": "travel destination"
                },
                "transportation": {
                    "type": "string",
                    "description": "transportation for travel. For example airplane, train, etc."
                }
            },
            "required": ["day", "destination", "transportation", "departure_point"]
        }
    }]
)

json_reponse = json.loads(completion.choices[0].message.function_call.arguments)
reservation_airplane(json_reponse)
