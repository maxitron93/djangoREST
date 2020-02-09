Learning django REST framework

## DRF Level 1

- <strong>Serialization</strong> and <strong>Deserialization</strong>

- How to create <strong>API Views</strong> using both Functions and Classes

- How to use <strong>Browsable API</strong>

- How to define <strong>validation criteria</strong> for user input

- How to represent <strong>nested relationships</strong> between entities within DRF

#### Serializers
Serializers allow complex datasets such as querysets and model instances to be converted to native Python data types that can then bea easily rendered intil useful formats like JSON: this process is known as Serialization of Data.

Serializers are a very important component of DRF, that we can easily use by employing the Serializer and ModelSerializer classes.

Serializers also provide deserialization, allowing parsed data the be converted back into complex types, after first validating the incoming data.

<strong>Essentially, serialization is converting from complex datatypes of Python data types, and deserialization is converting from Python data types to complex data types.</strong>

#### @api_view decorator

Django REST Framework provides two wrappers we can use to write API views:

- The ```@api_view``` decorator, for working with funciton-based API views

- The ```APIView``` class, for working with class-based API views

These wrappers will get all the code that is necessary to <strong>receive request instances</strong>, <strong>provide an appropriate response</strong> and <strong>handle exceptions</strong> such as the ParseError Exception that occurs when accessing request.data with malformed input.

#### APIView Class

As with 'pure' django, using View Classes makes it easy and fast to create reliable Web Apps, and by reusing common functionalities, it also helps keep our code DRY. 

#### Validation

Validation can be added to serializers. There are many pre-made validators, but we can also easily create our own validation logic in each serializer.

#### ModelSerializer Class

ModelSerializer allows us to speed up the creation of Serializers based on models we defined, providing us all the code that is needed for the most common development use cases.

A ModelSerializer is just a regular Serializer, except that:

- A set of default fields are automatically populated.
- A set of default validators are automatically populated.
- Default `.create()` and `update()` implementations are provided. 

