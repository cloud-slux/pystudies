# pystudies

##Creating a RESTFul API in Flask With JSON Web Token Authentication and Flask-SQLAlchemy
## https://www.youtube.com/watch?v=WxGBoY5iNXY

### hosted at heroku :)

### https://tembicipyquest.herokuapp.com/signup
####POST

{
	"name" : "Test",
	"email": "test@test.com",
	"password" : "test123",
	"phones" : [{
		"ddd": 11,
		"number": 123456789
	},
	{
		"ddd": 21,
		"number": 987653321
	}
	]
}

### https://tembicipyquest.herokuapp.com/signin
#### POST
{
	"email": "test@test.com",
	"password" : "test123"
}

###http://localhost:5000/user
#### GET
pass x-access-token on headers