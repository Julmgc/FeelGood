# <font color="green">**Feel Good API**</font>

This API is an perfume, beauty, skin and body care online platform, where clients and sellers can not only buy their products, but also to learn about each one with online courses that are linked to the product, an amazing selling programed system where the admin can show their sale prices and opportunities increasing the company profits.

## <font color="blue">**How to get started (global):**</font>

This api has been deployed to heroku, so here is the link to access the api.

```
https://sinta-se-bem.herokuapp.com/
```

Now you have to use a api client program, as insomnia, for example, so you can access and test the api.

## <font color="blue">**How to get started (locally):**</font>

To run this service in your local you need to do some steps, starting with cloning this project from gitlab. Click on this link:

```
https://gitlab.com/julmgc09/sinta-se-bem
```

Clone with the ssh option. After that, create a new directory in your local, inside this directory use:

```
git clone <paste the url copied>
```

Move in the directory created and run you code editor (you can use visual studio code, for instance).
Now open you terminal inside de project and if you have python previously installed in you machine, you need to start a virtual environment, run:

```
python -m venv venv --upgrade-deps
```

then enter the environment:

```
source venv/bin/activate
```

After that, you need to install the dependencies to run the code. Use:

```
pip install requirements.txt
```

```
python manage.py migrate
```

You will install all the dependencies you need this way. And now you can see the code.

Run the service locally:

```
python manage.py runserver
```

Now you have to use insomnia or other platform to access the API. Configure this platform with you localhost address in the port 8000.

- the service will be running at http://127.0.0.1:3000/

## <font color="green">Routes</font>

These are the endpoints you will need to access the API:

# <font color="blue">User</font>

The following endpoints will manage the user features, it can be of 3 kinds: admin, client, seller:

## POST /api/register/

Create a new user.

- Does not need authentication.

### Request example:

```
{
	"name": "Denise Belo",
	"email": "denise1@mail.com",
	"password": "123456",
	"first_name": "Denise",
	"last_name": "Belo",
	"cpf": "33333333333",
	"birthdate": "1988-09/23",
	"is_admin": true,
	"is_seller": false
}
```

### Response example:

- STATUS: 201 CREATED

```
{
  "uuid": "a1fffa5a-9574-4b41-b91f-205f266bacca",
  "email": "denise1@mail.com",
  "first_name": "Denise",
  "last_name": "Belo",
  "is_seller": false,
  "is_admin": true,
  "cpf": "33333333333",
  "birthdate": "1988-09/23",
  "is_active": true
}
```

## POST /api/login/

Generate login token that will be necessary to others endpoints.

- Does not need authentication.

### Request example:

```
{
	"email": "claudia@mail.com",
	"password": "123456"
}
```

### Response example:

- STATUS: 200 OK

```
{
  "token": "7b7809813f13d2f1b17e0d097dce2eece3327caf"
}
```

## GET /api/register/

List all registered users.

- Need admin authentication.
- Bearer token: admin login token.

### Request example:

```
No body
```

### Response example:

- STATUS: 200 OK

```
[
  {
    "uuid": "8174bd88-e976-42f0-b8d1-dc0577b31cc3",
    "email": "natiunirio@hotmail.com",
    "first_name": "Jose",
    "last_name": "Gaspar",
    "is_seller": false,
    "is_admin": true,
    "cpf": "12283723736",
    "birthdate": "1989-11-29",
    "is_active": true
  },
  {
    "uuid": "043879f4-25ab-4677-a898-bc7134b8ca67",
    "email": "c3@mail.com",
    "first_name": "comprador2",
    "last_name": "testando",
    "is_seller": false,
    "is_admin": false,
    "cpf": "12345678901",
    "birthdate": "2000-01-01",
    "is_active": true
  },
  {
    "uuid": "09795ad5-df70-4ea3-8f0a-05f5fe8fef49",
    "email": "natiunirio21@hotmail.com",
    "first_name": "Jose",
    "last_name": "Gaspar",
    "is_seller": true,
    "is_admin": false,
    "cpf": "12283723736",
    "birthdate": "1989-11-29",
    "is_active": true
  }
]
```

## GET /api/register/<user_id>/

List one registered user, filtered by it's id.

- Need admin authentication.
- Bearer token: admin login token.
- Use the user id in the route's parameter url.

### Request example:

```
no body
```

### Response example:

- STATUS: 200 OK

```
{
  "uuid": "8174bd88-e976-42f0-b8d1-dc0577b31cc3",
  "email": "natiunirio@hotmail.com",
  "first_name": "Jose",
  "last_name": "Gaspar",
  "is_seller": false,
  "is_admin": true,
  "cpf": "12283723736",
  "birthdate": "1989-11-29",
  "is_active": true
}
```

# <font color="blue">Address</font>

## PUT /api/address/

This route creates an address for the logged user.

- Need user authentication.
- Bearer token: user login token.

### Request example:

```
{
	"city": "riodejaneiro1",
	"street": "rua dos bobos",
	"house_number": "155",
	"state": "RJ",
	"cep": "20755-170",
	"country": "brasil"
}
```

### Response example:

- STATUS: 200 OK

```
{
  "id": "bd755fd9-e9b9-47e0-9663-2579dd91cb94",
  "street": "rua dos bobos",
  "house_number": 155,
  "city": "riodejaneiro1",
  "state": "RJ",
  "cep": "20755-170",
  "country": "brasil",
  "user": {
    "uuid": "1576a24c-c89e-4f73-8e63-b1b9eda10684",
    "email": "severino@mail.com",
    "first_name": "Severino",
    "last_name": "Francis",
    "is_seller": false,
    "is_admin": false,
    "cpf": "44444444444",
    "birthdate": "1989-11-29",
    "is_active": true
  }
}
```

## PATCH /api/address/

This update allows the logged user to update it's own address data.

- Need user authentication.
- Bearer token: user login token.

### Request example:

```
{
	"house_number": "5000"
}
```

### Response example:

- STATUS: 200 OK

```
{
  "id": "bd755fd9-e9b9-47e0-9663-2579dd91cb94",
  "street": "rua dos bobos",
  "house_number": 5000,
  "city": "riodejaneiro1",
  "state": "RJ",
  "cep": "20755-170",
  "country": "brasil",
  "user": {
    "uuid": "1576a24c-c89e-4f73-8e63-b1b9eda10684",
    "email": "severino@mail.com",
    "first_name": "Severino",
    "last_name": "Francis",
    "is_seller": false,
    "is_admin": false,
    "cpf": "44444444444",
    "birthdate": "1989-11-29",
    "is_active": true
  }
}
```

# <font color="blue">Products</font>

## POST /api/products/

This route allows admin to create one product.

- Need adm authentication.
- Bearer token: adm login token.

### Request example:

```
{
	"name": "teste",
	"description": "descrição do 1",
	"price_client": 101.00,
	"price_seller": 80.00,
	"quantity": 100,
	"expiration_date": "2024-01-01",
	"course_links": ["http://asd.com"],
	"categories": ["teste", "categoria 2"]
}
```

### Response example:

- STATUS: 201 CREATED

```
{
  "id": "268b7857-a32c-4d6b-8e4f-8c19d191f45d",
  "name": "teste",
  "description": "descrição do 1",
  "price_client": 101.0,
  "price_seller": 80.0,
  "quantity": 100,
  "expiration_date": "2024-01-01",
  "is_active": true,
  "sale": null,
  "course_links": [
    {
      "id": "f033c5d0-aed3-4dd7-8acc-85c7888592b3",
      "link": "http://asd.com"
    }
  ],
  "categories": [
    {
      "id": "7aa6cc40-fac2-4056-a97e-4c80adda81ed",
      "name": "categoria 2"
    },
    {
      "id": "ee04ebd4-2754-4ec9-ad0a-5dfe644b8ce4",
      "name": "teste"
    }
  ]
}
```

## GET /api/products/

List all registered products.

- Does not need authentication.

### Request example:

```
No body
```

### Response example:

- STATUS: 200 OK

```
[
  {
    "id": "8dcced73-8482-4e13-afb6-f13d3232493a",
    "name": "produto1",
    "description": "descrição do 1",
    "price_client": 100.0,
    "price_seller": 80.0,
    "quantity": 100,
    "expiration_date": "2024-01-01",
    "is_active": true,
    "sale": null,
    "course_links": [],
    "categories": [
      {
        "id": "58edf984-4bcc-4c85-9390-0c2d67867815",
        "name": "teste"
      },
      {
        "id": "7174aabe-8281-4efd-bc8c-3a012fdcd6d8",
        "name": "categoria 1"
      }
    ]
  },
  {
    "id": "a273c525-ccd9-4d97-8dbf-0ebe7e3da68e",
    "name": "produto2",
    "description": "descrição do 1",
    "price_client": 101.0,
    "price_seller": 80.0,
    "quantity": 100,
    "expiration_date": "2024-01-01",
    "is_active": true,
    "sale": null,
    "course_links": [
      {
        "id": "c243b7d1-21df-412c-9c86-c3a70c56c48b",
        "link": "http://asd.com"
      }
    ],
  },
]
```

## GET /api/products/<product_id>

List one registered product, filtered by it's id.

- Does not need authentication.

### Request example:

```
No body
```

### Response example:

- STATUS: 200 OK

```
{
  "id": "0abf65c8-a374-4498-be27-c2971a48b214",
  "name": "produto1",
  "description": "descrição do 1",
  "price_client": 100.0,
  "price_seller": 80.0,
  "quantity": 100,
  "expiration_date": "2024-01-01",
  "is_active": true,
  "sale": null,
  "course_links": [
    {
      "id": "c243b7d1-21df-412c-9c86-c3a70c56c48b",
      "link": "http://asd.com"
    }
  ],
  "categories": []
}
```

## PUT /api/products/<product_id>/

Update one registered product data, filtered by it's id.

- Need admin authentication.
- Bearer token: admin login token.
- Use the product id in the route's parameter url.

### Request example:

```
{
	"name": "produto1",
	"description": "descrição do 1",
	"price_client": 100.00,
	"price_seller": 80.00,
	"quantity": 100,
	"expiration_date": "2024-01-01",
	"course_links": ["http://asd.com"]
}
```

### Response example:

- STATUS: 200 OK

```
{
  "id": "0abf65c8-a374-4498-be27-c2971a48b214",
  "name": "produto1",
  "description": "descrição do 1",
  "price_client": 100.0,
  "price_seller": 80.0,
  "quantity": 100,
  "expiration_date": "2024-01-01",
  "is_active": true,
  "sale": null,
  "course_links": [
    {
      "id": "c243b7d1-21df-412c-9c86-c3a70c56c48b",
      "link": "http://asd.com"
    }
  ],
  "categories": []
}
```

## DELETE /api/products/<product_id>/

Delete one registered product, filtered by it's id.

- Need admin authentication.
- Bearer token: admin login token.
- Use the product id in the route's parameter url.

### Request example:

```
no body
```

### Response example:

- STATUS: 204 NO CONTENT

```
No body
```

# <font color="blue">Course_link</font>

## POST /api/course/

This route creates a course.

- Need admin authentication.
- Bearer token: admin login token.

### Request example:

```
{
	"link": "http://asd2d.com"
}
```

### Response example:

- STATUS: 201 CREATED

```
{
  "id": "ba17e1df-64e4-4b41-9c5f-66daf819150e",
  "link": "http://asd2d.com"
}
```

## POST /api/course/course_id/add/

This route adds the link course in one previously created product.

- Need adm authentication.
- Bearer token: adm login token.
- Use the course id in the route's parameter url.

### Request example:

```
{
	"product_id": "0abf65c8-a374-4498-be27-c2971a48b214"
}
```

### Response example:

- STATUS: 200 OK

```
{
  "id": "0abf65c8-a374-4498-be27-c2971a48b214",
  "name": "produto1",
  "description": "descrição do 1",
  "price_client": 100.0,
  "price_seller": 80.0,
  "quantity": 100,
  "expiration_date": "2024-01-01",
  "is_active": true,
  "sale": null,
  "course_links": [
    {
      "id": "c243b7d1-21df-412c-9c86-c3a70c56c48b",
      "link": "http://asd.com"
    },
    {
      "id": "3e5e0b06-ae99-473f-a3dd-57f420c63883",
      "link": "http://asd23.com"
    }
  ],
  "categories": []
}
```

## GET /api/course/

List all registered courses.

- Does not need authentication.

### Request example:

```
    no body
```

### Response example:

- STATUS: 200 OK

```
[
  {
    "id": "c243b7d1-21df-412c-9c86-c3a70c56c48b",
    "link": "http://asd.com"
  },
  {
    "id": "1e6deddb-fd45-4665-8c54-086e4bd4566a",
    "link": "http://asd5.com"
  },
  {
    "id": "3e5e0b06-ae99-473f-a3dd-57f420c63883",
    "link": "http://asd23.com"
  },
  {
    "id": "ba17e1df-64e4-4b41-9c5f-66daf819150e",
    "link": "http://asd2d.com"
  }
]
```

## GET /api/course/<course_id>/

List one course, filtered by it's id.

- Does not need authentication.

### Request example:

```
No body
```

### Response example:

- STATUS: 200 OK

```
{
  "id": "c243b7d1-21df-412c-9c86-c3a70c56c48b",
  "link": "http://asd.com"
}
```

## PATCH /api/course/<course_id>/

Updates the one course data, filtered by it's id.

- Need adm authentication.
- Bearer token: adm login token.
- Use the course id in the route's parameter url.

### Request example:

```
{
	"link": "http://asd23.com"
}
```

### Response example:

- STATUS: 200 OK

```
{
  "id": "3e5e0b06-ae99-473f-a3dd-57f420c63883",
  "link": "http://asd23.com"
}
```

# <font color="blue">Sale</font>

## POST /api/sale/

Use this route to create sales.

- Need adm authentication.
- Bearer token: adm login token.

### Request example:

```
{
	"discount_percentage": 9.0,
	"initial_datetime": "2022-09-05 06:00",
	"final_datetime": "2022-09-05 06:00"
}
```

### Response example:

- STATUS: 201 CREATED

```
{
  "id": "a0839f5a-2c86-4839-8091-97440ae567fb",
  "discount_percentage": 9.0,
  "is_active": true,
  "initial_datetime": "2022-09-05T06:00:00Z",
  "final_datetime": "2022-09-05T06:00:00Z"
}
```

## GET /api/sale/<sale_id>/

This route get just one sale, filtered by it's id.

- Does not need authentication.
- Use the sale id in the route's parameter url.

### Request example:

```
    no body
```

### Response example:

- STATUS: 200 OK

```
{
  "id": "2471530b-6a5e-4adb-b6e6-af5aa412e24a",
  "discount_percentage": 6.0,
  "is_active": true,
  "initial_datetime": "2022-09-05T06:00:00Z",
  "final_datetime": "2022-09-05T06:00:00Z"
}
```

## GET /api/sale/

This route get all registered salrs.

- Does not need authentication.

### Request example:

```
    no body
```

### Response example:

- STATUS: 200 OK

```
[
  {
    "id": "2471530b-6a5e-4adb-b6e6-af5aa412e24a",
    "discount_percentage": 6.0,
    "is_active": true,
    "initial_datetime": "2022-09-05T06:00:00Z",
    "final_datetime": "2022-09-05T06:00:00Z"
  },
  {
    "id": "a0839f5a-2c86-4839-8091-97440ae567fb",
    "discount_percentage": 9.0,
    "is_active": true,
    "initial_datetime": "2022-09-05T06:00:00Z",
    "final_datetime": "2022-09-05T06:00:00Z"
  }
]
```

## PATCH /api/sale/<sale_id>/

This update allows the adm to update one sale data.

- Need adm authentication.
- Bearer token: adm login token.
- Use the sale id in the route's parameter url.

### Request example:

```
{
	"discount_percentage": 6.0
}
```

### Response example:

- STATUS: 200 OK

```
{
  "id": "2471530b-6a5e-4adb-b6e6-af5aa412e24a",
  "discount_percentage": 6.0,
  "is_active": true,
  "initial_datetime": "2022-09-05T06:00:00Z",
  "final_datetime": "2022-09-05T06:00:00Z"
}
```

# <font color="blue">Payment</font>

## POST /api/payment/

This route creates payment methods.

- Need user self authentication.
- Bearer token: user login token.

### Request example:

```
{
	"payment_method": "credit",
	"card_number": "12345678123456",
	"cardholders_name": "Teste Resto",
	"card_expiration_date": "2122-04-01",
	"cvv": 456
}
```

### Response example:

- STATUS: 201 CREATED

```
{
  "id": "45b84c81-384b-4dca-8d53-82c901fbb0c2",
  "card_number_info": "**********3456",
  "customer": {
    "uuid": "1576a24c-c89e-4f73-8e63-b1b9eda10684",
    "email": "severino@mail.com",
    "first_name": "Severino",
    "last_name": "Francis",
    "is_seller": false,
    "is_admin": false,
    "cpf": "44444444444",
    "birthdate": "1989-11-29",
    "is_active": true
  },
  "payment_method": "credit",
  "cardholders_name": "Teste Resto",
  "card_expiration_date": "2122-04-01",
  "cvv": "456",
  "is_active": true
}
```

## GET /api/payment/

List all registered payment methods of the self user.

- Need user self authentication.
- Bearer token: user login token.

### Request example:

```
No body
```

### Response example:

- STATUS: 200 OK

```
[
  {
    "id": "45b84c81-384b-4dca-8d53-82c901fbb0c2",
    "card_number_info": "**********3456",
    "customer": {
      "uuid": "1576a24c-c89e-4f73-8e63-b1b9eda10684",
      "email": "severino@mail.com",
      "first_name": "Severino",
      "last_name": "Francis",
      "is_seller": false,
      "is_admin": false,
      "cpf": "44444444444",
      "birthdate": "1989-11-29",
      "is_active": true
    },
    "payment_method": "credit",
    "cardholders_name": "Teste Resto",
    "card_expiration_date": "2122-04-01",
    "cvv": "456",
    "is_active": true
  }
]
```

## GET /api/payment/<payment_id>/

List one registered payment method of the self user, filtered by it's id.

- Need user self authentication.
- Bearer token: user login token.
- Use payment id in the url parameters.

### Request example:

```
No body
```

### Response example:

- STATUS: 200 OK

```
[
  {
    "id": "45b84c81-384b-4dca-8d53-82c901fbb0c2",
    "card_number_info": "**********3456",
    "customer": {
      "uuid": "1576a24c-c89e-4f73-8e63-b1b9eda10684",
      "email": "severino@mail.com",
      "first_name": "Severino",
      "last_name": "Francis",
      "is_seller": false,
      "is_admin": false,
      "cpf": "44444444444",
      "birthdate": "1989-11-29",
      "is_active": true
    },
    "payment_method": "credit",
    "cardholders_name": "Teste Resto",
    "card_expiration_date": "2122-04-01",
    "cvv": "456",
    "is_active": true
  }
]
```

## DELETE /api/payment/<payment_id>/

Delete one payment method, filtered by it's id.

- Need self user authentication.
- Bearer token: user login token.
- Use the payment id in the route's parameter url.

### Request example:

```
No body
```

### Response example:

- STATUS: 204 NO CONTENT

```
No body returned for response
```

# <font color="blue">Transaction</font>

## POST /api/transaction/

Create a buying transaction.

- Need self user authentication.
- Bearer token: user login token.

### Request example:

```
{
	"payment": {
		"id": "fbd1666c-9cc9-4861-9877-0cf6d6921d44"
	},
	"products": [
		{
			"id": "0abf65c8-a374-4498-be27-c2971a48b214",
			"quantity": 10
		}
	]
}
```

### Response example:

- STATUS: 201 CREATED

```
{
  "id": "281ac551-d7e9-4d4f-8db5-bbb0275dcf89",
  "user": {
    "uuid": "1576a24c-c89e-4f73-8e63-b1b9eda10684",
    "email": "severino@mail.com",
    "first_name": "Severino",
    "last_name": "Francis",
    "is_seller": false,
    "is_admin": false,
    "cpf": "44444444444",
    "birthdate": "1989-11-29",
    "is_active": true
  },
  "amount": 1000.0,
  "created_at": "2022-03-31T21:26:57.983781Z",
  "payment": {
    "id": "fbd1666c-9cc9-4861-9877-0cf6d6921d44",
    "payment_method": "credit",
    "card_number": "12345678123456",
    "cardholders_name": "Teste Resto",
    "card_expiration_date": "2122-04-01",
    "cvv": "456",
    "is_active": true,
    "customer": "ebef5265-6b0a-4f44-8c19-d0c11d8fcd3f"
  }
}
```

## GET /api/transaction/

This route list all registered transactions.

- Need admin or self user authentication.
- Bearer token: admin or self user login token.

### Request example:

```
No body
```

### Response example:

- STATUS: 200 OK

```
[
  {
    "id": "d294c493-3b8c-4b0d-87ad-55d7cc334325",
    "user": {
      "uuid": "8cc2e26a-65b1-469c-8d82-f89456bfa6a7",
      "email": "natiunirio98@hotmail.com",
      "first_name": "Jose",
      "last_name": "Gaspar",
      "is_seller": false,
      "is_admin": true,
      "cpf": "12283723736",
      "birthdate": "1989-11-29",
      "is_active": true
    },
    "amount": 1000.0,
    "created_at": "2022-03-31T00:33:00.074758Z",
    "payment": {
      "id": "fbd1666c-9cc9-4861-9877-0cf6d6921d44",
      "payment_method": "credit",
      "card_number": "12345678123456",
      "cardholders_name": "Teste Resto",
      "card_expiration_date": "2122-04-01",
      "cvv": "456",
      "is_active": true,
      "customer": "ebef5265-6b0a-4f44-8c19-d0c11d8fcd3f"
    }
  },
  {
    "id": "da994758-9842-4e93-9e9e-af1a7fc5eb56",
    "user": {
      "uuid": "8cc2e26a-65b1-469c-8d82-f89456bfa6a7",
      "email": "natiunirio98@hotmail.com",
      "first_name": "Jose",
      "last_name": "Gaspar",
      "is_seller": false,
      "is_admin": true,
      "cpf": "12283723736",
      "birthdate": "1989-11-29",
      "is_active": true
    },
    "amount": 1000.0,
    "created_at": "2022-03-31T01:54:31.148795Z",
    "payment": {
      "id": "fbd1666c-9cc9-4861-9877-0cf6d6921d44",
      "payment_method": "credit",
      "card_number": "12345678123456",
      "cardholders_name": "Teste Resto",
      "card_expiration_date": "2122-04-01",
      "cvv": "456",
      "is_active": true,
      "customer": "ebef5265-6b0a-4f44-8c19-d0c11d8fcd3f"
    }
  },
]
```

## GET /api/transaction/<transaction_id>/

This route get just one transaction, filtered by it's id.

- Need admin or self user authentication.
- Bearer token: admin or self user login token.
- Use transaction id in the url parameters.

### Request example:

```
    no body
```

### Response example:

- STATUS: 200 OK

```
{
  "id": "d294c493-3b8c-4b0d-87ad-55d7cc334325",
  "user": {
    "uuid": "8cc2e26a-65b1-469c-8d82-f89456bfa6a7",
    "email": "natiunirio98@hotmail.com",
    "first_name": "Jose",
    "last_name": "Gaspar",
    "is_seller": false,
    "is_admin": true,
    "cpf": "12283723736",
    "birthdate": "1989-11-29",
    "is_active": true
  },
  "amount": 1000.0,
  "created_at": "2022-03-31T00:33:00.074758Z",
  "payment": {
    "id": "fbd1666c-9cc9-4861-9877-0cf6d6921d44",
    "payment_method": "credit",
    "card_number": "12345678123456",
    "cardholders_name": "Teste Resto",
    "card_expiration_date": "2122-04-01",
    "cvv": "456",
    "is_active": true,
    "customer": "ebef5265-6b0a-4f44-8c19-d0c11d8fcd3f"
  }
}
```

## GET /api/order/transaction/transaction_id/

This route gets an order by the transaction id.

- Need admin or self user authentication.
- Bearer token: admin or self user login token.
- Use transaction id in the url parameters.

### Request example:

```
    no body
```

### Response example:

- STATUS: 200 OK

```
{
  "id": "d402c0fe-bcbc-45dc-b621-418beff86468",
  "quantity": 10,
  "amount": "1000.00",
  "product": {
    "id": "0abf65c8-a374-4498-be27-c2971a48b214",
    "name": "produto1",
    "description": "descrição do 1",
    "price_client": 100.0,
    "price_seller": 80.0,
    "quantity": 90,
    "expiration_date": "2024-01-01",
    "is_active": true,
    "sale": null,
    "course_links": [
      "c243b7d1-21df-412c-9c86-c3a70c56c48b",
      "3e5e0b06-ae99-473f-a3dd-57f420c63883"
    ],
    "categories": []
  },
  "transaction": {
    "id": "d294c493-3b8c-4b0d-87ad-55d7cc334325",
    "amount": 1000.0,
    "created_at": "2022-03-31T00:33:00.074758Z",
    "payment": "fbd1666c-9cc9-4861-9877-0cf6d6921d44",
    "user": "8cc2e26a-65b1-469c-8d82-f89456bfa6a7"
  },
  "customer": {
    "uuid": "8cc2e26a-65b1-469c-8d82-f89456bfa6a7",
    "last_login": "2022-03-30T22:47:36.661383Z",
    "is_superuser": false,
    "is_staff": false,
    "date_joined": "2022-03-30T22:47:36.661383Z",
    "first_name": "Jose",
    "last_name": "Gaspar",
    "email": "natiunirio98@hotmail.com",
    "password": "pbkdf2_sha256$320000$Qba5OObmA716HhOhz1AFoO$BFvT1kYOeKxBoANRTahZJqDMqH3p6KXzh6QCI+vM35s=",
    "cpf": "12283723736",
    "birthdate": "1989-11-29",
    "is_admin": true,
    "is_seller": false,
    "is_active": true,
    "username": null,
    "address": null,
    "groups": [],
    "user_permissions": []
  }
}
```

# <font color="blue">Invoice</font>

## GET /api/invoice/

Lists all registered invoices.

- Need admin authentication.
- Bearer token: admin login token.

### Request example:

```
No body
```

### Response example:

- STATUS: 200 OK

```
[
  {
    "id": "436756c2-79b2-4b6a-97af-b1ea0fab7010",
    "number": "99962469152886249096716953666275077788979796",
    "transaction": {
      "id": "d294c493-3b8c-4b0d-87ad-55d7cc334325",
      "amount": 1000.0,
      "created_at": "2022-03-31T00:33:00.074758Z",
      "payment": "fbd1666c-9cc9-4861-9877-0cf6d6921d44",
      "user": "8cc2e26a-65b1-469c-8d82-f89456bfa6a7"
    }
  },
  {
    "id": "7331b171-befe-4cd3-a890-f5c5d407978c",
    "number": "99973355146896646916383525692069276978571054",
    "transaction": {
      "id": "da994758-9842-4e93-9e9e-af1a7fc5eb56",
      "amount": 1000.0,
      "created_at": "2022-03-31T01:54:31.148795Z",
      "payment": "fbd1666c-9cc9-4861-9877-0cf6d6921d44",
      "user": "8cc2e26a-65b1-469c-8d82-f89456bfa6a7"
    }
  },
  {
    "id": "06231408-83bb-401a-ad50-57c78c2bc0cc",
    "number": "99917883361451842396923824583635821012356873",
    "transaction": {
      "id": "66b0830e-cd4a-432d-b2df-62ff9cbd839e",
      "amount": 1000.0,
      "created_at": "2022-03-31T12:50:36.452715Z",
      "payment": "fbd1666c-9cc9-4861-9877-0cf6d6921d44",
      "user": "ebef5265-6b0a-4f44-8c19-d0c11d8fcd3f"
    }
  },
]
```

## GET /api/invoice/<invoice_id>/

Lists one registered invoices, filtered by it's id.

- Need admin or self user authentication.
- Bearer token: admin or self user login token.

### Request example:

```
No body
```

### Response example:

- STATUS: 200 OK

```
{
  "id": "436756c2-79b2-4b6a-97af-b1ea0fab7010",
  "number": "99962469152886249096716953666275077788979796",
  "transaction": {
    "id": "d294c493-3b8c-4b0d-87ad-55d7cc334325",
    "amount": 1000.0,
    "created_at": "2022-03-31T00:33:00.074758Z",
    "payment": "fbd1666c-9cc9-4861-9877-0cf6d6921d44",
    "user": "8cc2e26a-65b1-469c-8d82-f89456bfa6a7"
  }
}
```

# <font color="blue">Product_review</font>

## POST /api/productReview/

This route creates a review to one product.

- Need user (client or seller) authentication.
- Bearer token: user (client or seller) login token.

### Request example:

```
{
	"comment": "W product",
	"score": 4.0,
	"product": "0abf65c8-a374-4498-be27-c2971a48b214"
}
```

### Response example:

- STATUS: 201 CREATED

```
{
  "id": "897de8d6-e364-4a95-a0e9-d8ca32b57fb2",
  "comment": "W product",
  "score": 4.0,
  "user": {
    "uuid": "1576a24c-c89e-4f73-8e63-b1b9eda10684",
    "email": "severino@mail.com",
    "first_name": "Severino",
    "last_name": "Francis",
    "is_seller": false,
    "is_admin": false,
    "cpf": "44444444444",
    "birthdate": "1989-11-29",
    "is_active": true
  },
  "product": {
    "id": "0abf65c8-a374-4498-be27-c2971a48b214",
    "name": "produto1",
    "description": "descrição do 1",
    "price_client": 100.0,
    "price_seller": 80.0,
    "quantity": 80,
    "expiration_date": "2024-01-01",
    "is_active": true,
    "sale": null,
    "course_links": [
      "c243b7d1-21df-412c-9c86-c3a70c56c48b",
      "3e5e0b06-ae99-473f-a3dd-57f420c63883"
    ],
    "categories": []
  }
}
```

## PATCH /api/productReview/productReview_id/

Updates the product review data.

- Need user (client or seller) authentication.
- Bearer token: user (client or seller) login token.
- Use the productReview id in the route's parameter url.

### Request example:

```
{
	"comment": "XXX product",
	"score": 4.0,
	"product": "0abf65c8-a374-4498-be27-c2971a48b214"
}
```

### Response example:

- STATUS: 200 OK

```
{
  "id": "897de8d6-e364-4a95-a0e9-d8ca32b57fb2",
  "comment": "XXX product",
  "score": 4.0,
  "user": "1576a24c-c89e-4f73-8e63-b1b9eda10684",
  "product": "0abf65c8-a374-4498-be27-c2971a48b214"
}
```

## GET /api/productReview/

List all registered reviews.

- Does not need authentication.

### Request example:

```
no body
```

### Response example:

- STATUS: 200 OK

```
[
  {
    "id": "240c4df4-e379-49dd-b951-b0fb3bbb6f18",
    "comment": "XXX product",
    "score": 4.0,
    "user": "ebef5265-6b0a-4f44-8c19-d0c11d8fcd3f",
    "product": "0abf65c8-a374-4498-be27-c2971a48b214"
  },
  {
    "id": "897de8d6-e364-4a95-a0e9-d8ca32b57fb2",
    "comment": "XXX product",
    "score": 4.0,
    "user": "1576a24c-c89e-4f73-8e63-b1b9eda10684",
    "product": "0abf65c8-a374-4498-be27-c2971a48b214"
  }
]
```

## GET /api/productReview/<productReview_id>

List one registered review, filtered by it's id.

- Does not need authentication.
- Use the productReview id in the url parameters.

### Request example:

```
no body
```

### Response example:

- STATUS: 200 OK

```
{
  "id": "240c4df4-e379-49dd-b951-b0fb3bbb6f18",
  "comment": "XXX product",
  "score": 4.0,
  "user": "ebef5265-6b0a-4f44-8c19-d0c11d8fcd3f",
  "product": "0abf65c8-a374-4498-be27-c2971a48b214"
}
```

# <font color="blue">Category</font>

## POST /api/category/

Create a new category of products.

- Need admin authentication.
- Bearer token: admin login token.

### Request example:

```
{
	"name": "perfume jador"
}
```

### Response example:

- STATUS: 201 CREATED

```
{
  "id": "b30a1274-e86f-4b3f-8e8a-c14798b99c84",
  "name": "perfume jador"
}
```

## GET /api/category/

List all registered categories.

- Need logged user authentication.
- Bearer token: logged user login token.

### Request example:

```
no body
```

### Response example:

- STATUS: 200 OK

```
[
  {
    "id": "58edf984-4bcc-4c85-9390-0c2d67867815",
    "name": "teste"
  },
  {
    "id": "7174aabe-8281-4efd-bc8c-3a012fdcd6d8",
    "name": "categoria 1"
  },
  {
    "id": "0b0d1ad3-9a43-4cea-b3e5-03ae8308ce64",
    "name": "categoria 2"
  },
  {
    "id": "51781c0c-84fd-4def-9e78-123379d04a27",
    "name": "baton"
  },
]
```

## GET /api/category/category_id/

List a specific category, filtered by it's id.

- Does not need authentication.

### Request example:

```
no body
```

### Response example:

- STATUS: 200 OK

```
{
  "id": "ce519df5-0697-41b4-b4b6-f8eea12c4f3e",
  "name": "perfume channel"
}
```

## PATCH /api/category/<category_id>/

This update allows the admin to update one category data, filtered by it's id.

- Need admin authentication.
- Bearer token: admin login token.
- Use the category id in the route's parameter url.

### Request example:

```
{
	"name": "perfume channel"
}
```

### Response example:

- STATUS: 200 OK

```
{
  "id": "ce519df5-0697-41b4-b4b6-f8eea12c4f3e",
  "name": "perfume channel"
}
```

## Technologies

- Python;
- Django;
- Django rest_framework;
- Gunicorn;
- Psycopg2;
- db.sqlite3;
- Heroku;

## Licenses

MIT
