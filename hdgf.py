# Dictionaries

studentid = {
    "101" : "sakib",
    "102" : "sakibkj",
    "103" : "sakibvf",
    "104" : "sakibpl",
    "105" : "sakibld",
}
print(studentid ["101"])



#error


studentid = {
    "101" : "sakib",
    "102" : "sakibkj",
    "103" : "sakibvf",
    "104" : "sakibpl",
    "105" : "sakibld",
}
print(studentid.get("106","not a vallid kye"))
print(studentid.get("105","not a vallid kye"))