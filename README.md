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

## DRF Level 2

- Use <strong>GenericAPIView</strong> and <strong>Mixin</strong> classes

- Customize <strong>Generic</strong> class-based views

- Group the results provided by your API with a <strong>pagination</strong> system

- Secure your web API with a <strong>Permissions</strong> System

#### GenericAPIView and Mixins

CRUD operations in a model-backed API will be implemented in the same way in most cases. GenericAPIView extends the APIView class, adding to this some very useful methods and attributes, so we don't have to keep writing the same code again and again.

The GenericAPIView class is often used with Mixins - classes that provide further pre-built functionality to our views. Mixin classes provide <strong>action methods</strong> such as ```.list()``` or ```.create()``` rather than defining the handler methods, such as ```.get()``` or ```.post()``` directly, as we did using the APIView class.

#### Concrete View Classes

Extension of the GenericAPIView class and this Mixins that offer the functionality that the class is meant to provide. 

For example, RetrieveUpdateAPIView will extend the <strong>GenericAPIView</strong> class plus both <strong>RetrieveModelMixin</strong> and <strong>UpdateModelMixin</strong>.

These are the fastest to write, and fastest to read, but are also the most 'magical'. It's important to know how they can be used, and how they can be customised when needed.

#### Permissions

Can be used to secure REST API endpoints. This menas we can grant access to certain APIs based on <strong>authentication</strong> and <strong>authorization</strong>.

#### Pagination

Pagination allows us to group the results provided by our API's List Views to make it easier for users and clients to retreive our data.

## DRF Level 3

- Knowledge of the main <strong>Authentication</strong> methods

- Set up <strong>Registration</strong> and <strong>Authentication</strong> via REST

- How to use <strong>Django-REST-Auth</strong>

- Knowledge of <strong>Viewset</strong> and <strong>Router</strong> classes

- How to do <strong>Filtering</strong> via DRF

- How to write <strong>automated tests</strong> with Django and DRF

- How to <strong>extend Django's User Model</strong> with a custom Profile Model

#### Signals

Signals allow certain senders to notify Receivers that an action has taken place elsewhere inthe framework. e.g. We can use signals to create a new instance of Profile when a new instance of User is created.
