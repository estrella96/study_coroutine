import json
student={
    "name": "jasa",
    "age": 18
}
stu_json=json.dumps(student)

stu_py=json.loads(stu_json)

