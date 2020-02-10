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

#### Authentication

Authentication is the system that lets us associate a series of identification credentials to an incoming request, obtaining critical information such as the specific user who sent the request.

We can use this in conjunction with the permission system to decide whether or not to accept the incomming request, for exaple, based on the type of user who sent it.

Authentication is always run at the start of the views, before the authorization check occurs, and before any other code is allowed to be executed.

Authentication --> Authorization (permission) --> Code

Authentication by itself won't allow or disallow incoming requests, it simply identifies the credentials that the request was made with.

DRF provides different authentication systems out of the box. But we can also use third party packages to implement other systems, like JWT.

- <strong>Basic authentication</strong>: The most primitave and least secure authentication system provided by DRF. The request/response cycle looks like this:
    
    1) The client makes a HTTP request to the server

    2) The server responds with a HTTP401 Unauthorized response containing the WWW-Authenticate header, exaplining how to authenticate (e.g. WWW-Authenticate-Basic)

    3) The client sends its auth credentials in base64 with the Authorization header. Authentication credentials are unencrypted

    4) The server evaluates the access credentials and repsponds with 200 or 403, thereby authorizing or denying the client's request

- <strong>Token authentication</strong>: This is the ideal system for authenticating smartphone and desktop clients. The request.response flow looks like this:
    
    1) The client sends its authentication credentials once

    2) The server checks the credentials, and if they are valid it creates an exclusive signed token and sends it back to the client as a response

    3) The client sends this token within the Authorization Header of every following request

    4) The server checks the received token and if valid, allows the request to proceed

    It's common to save this authentication token in either a cookie or in the browser's localStorage. But saving the authentication token to localStorage is very dangerous, as it makes it vulnerable to XSS attacks.

    Using a httpOnly cookie is much safer because this way the token can't be accessed via JavaScript, but doing it this way means you lose the flexibility that you would get if you used localStorage.

    JSON Web Token is a new standard which can be used for token-based authentication. One of the main differences with other token-based standards is that because of their structure, JWT tokens don't require databas validation.

- <strong>Session authentication</strong>: Django REST Framework's official documentation suggests to use session authentication. This authentication scheme uses Django's default session backend for authentication. It's the safest and most appropriate way for authenticating AJAX clients that are running in the same session context as your website, and uses a combination of Sessions and Cookies. The request/response cycle looks like this:

    1) The user sends their authentication credentials, typically using a Login Form
    2) The server checks the data and if correct, it creates a corresponding Session Object that will be saved in the database, sending back to the client a Session ID
    3) The Session ID gets saved in a cookin in the browser and will be part of every future request to the server, that will check it everytime
    4) When the client logs out, the Session ID is destroyed by both the client and the server, and a new one will be created at the next login

    If successfully authenticated using Session Authentication, Django will provide us the corresponding User Object, accessible via request.user. For non-authorized users, an AnonymousUser instance will be provided instead.

    Important: Once authenticated via session auth, Django will require a valid CSRF token to be sent for any <strong>unsafe</strong> HTTP method request such as PUT, PATCH, POST, DELETE. The CSRF token is an important cross-site request forgery vulnerability protection.

