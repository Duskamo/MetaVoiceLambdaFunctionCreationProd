jsonDict = {
    'category': 'Select',
    'intents': [{'intent': 'intent', 'response': 'mok', 'utterances': {
        '1': 'mko',
        '3': 'omk',
        '2': 'mok',
        '5': 'mok',
        '4': 'mko',
        }}],
    'skillName': 'mok',
    'firstName': 'kmo',
    'lastName': 'mko',
    'longDescription': 'kmo',
    'code': '''def create_response(text, shouldEndSession):
    return {
        \'version\': \'1.0\',
        \'sessionAttributes\': {},
        \'response\': {
          \'outputSpeech\': {
              \'type\': \'PlainText\',
              \'text\': text
          },
          \'card\': {
              \'type\': \'Simple\',
              \'title\': \'mok\',
              \'content\': text
          },
          \'reprompt\': {
              \'outputSpeech\': {
                  \'type\': \'PlainText\',
                  \'text\': "text"
              }
          },
          \'shouldEndSession\': shouldEndSession
        }
    }


def lambda_handler(event, context):

    #on launch request prompt user to ask for help
    if event[\'request\'][\'type\'] == \'LaunchRequest\':
        return create_response(\'If you dont know how to use me you can ask for help by saying help\', False)

    #give user utterances
    elif event[\'request\'][\'intent\'][\'name\'] == \'Help\':
        return create_response(\'There are several commands, try saying mko\', False)

    #end session
    elif event[\'request\'][\'type\'] == \'SessionEndedRequest\':
        return create_response(\'\', True)

    #end session
    elif event[\'request\'][\'intent\'][\'name\'] == \'endSession\':
        return create_response(\'\', True)

    #user defined intents
    #paste content here
    elif event[\'request\'][\'intent\'][\'name\'] == \'intent\':
        return create_response(\'mok\', True)

''',
    'template': 'Alexa Interaction',
    'invocationName': 'mko',
    'keywords': 'mok',
    'shortDescription': 'mok',
    'email': 'mok',
    }
