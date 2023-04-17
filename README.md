# tutorials-api

Basic CRUD for Tutorials

- CREATE
  POST: http://localhost:8000/api/tutorials
  Example of body:
  {
    "title": "React master course",
    "description": "In this course you will create frontend web components using React library",
    "published": true
  }
  

- GET_ALL
  GET: http://localhost:8000/api/tutorials
  
- GET_A_SINGLE
  GET: http://localhost:8000/api/tutorials/3
  
- UPDATE:
  PUT: http://localhost:8000/api/tutorials/3
  Example:
  {
    "title": "Django REST Framework from beginner to master",
    "description": "In this course you will learn how to create robust web APIs with Django REST Framework",
    "published": true
  }
  
- SEARCH_BY_PARAM_IN_FIELD
  GET: http://localhost:8000/api/tutorials?title=angular
  
- GET_PUBLISHED
  GET: http://localhost:8000/api/tutorials/published
  
- DELETE_ONE
  DELETE: http://localhost:8000/api/tutorials/4
  
- DELETE_ALL
  DELETE: http://localhost:8000/api/tutorials
