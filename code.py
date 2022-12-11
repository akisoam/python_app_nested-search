akashData = {
    'name': "Akash Soam",
    'address': {
        'city': "Bengaluru",
        'pin': 560037,
        'contact': {
            'phone': 91,
            'mail': {
                'gmail': 'gmail.com',
                'outlook': 'outlook.com'
            }
        }
    }
}

def getValue(property, input):
    if property in input.keys():
        # get value from root level
        value = input[property];
        #print(value)
        return value;
    else:
        # get value from nested objects
        return getFromNestedObjects(property, input);

def getFromNestedObjects(property, input):
    for key in input:
        if isinstance(input[key], dict):
            nestedObject = input[key];
            return getValue(property, nestedObject)

print(getValue('gmail', akashData))
