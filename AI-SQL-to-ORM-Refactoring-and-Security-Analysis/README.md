# AI: SQL to ORM Refactoring and Security Analysis

## Overview

This task explores how procedural database code using raw SQL can be refactored into a more object-oriented design using SQLAlchemy ORM.

The original version uses direct SQL statements with a MySQL cursor. The refactored version uses a SQLAlchemy declarative model, ORM Session, and Python objects to represent and manipulate database records.

## Files

- `initial_code.py` - original procedural database code using raw SQL
- `refactored_code.py` - SQLAlchemy ORM version using SQLAlchemy 1.4.x
- `README.md` - documentation for the task

## Main Changes

The refactored version introduces a `User` model that maps Python attributes to database table columns. Database operations such as create, query, update, and delete are handled through a SQLAlchemy Session instead of writing SQL strings directly.

A `UserManager` class is also used to organize database operations in one place and make the code easier to maintain.

## Security

The original code already uses parameterized SQL queries, which protect against standard SQL injection attacks.

The ORM version keeps this protection because SQLAlchemy also uses parameter binding by default when building normal ORM queries. It also reduces the chance that a developer will accidentally construct unsafe SQL strings manually.

## Maintainability and Abstraction

With the ORM approach, database rows are represented as Python objects. Instead of manually translating between tuples, SQL statements, and application logic, the program works with objects such as `User`.

This makes the code easier to read, organize, and change because the database structure and related behavior are represented through Python classes.

## Verification

The refactored code was tested locally using SQLAlchemy 1.4.54 and an in-memory SQLite database.

The test confirmed that the application could:

- create users
- query a user by username
- update a user's email
- list users
- delete a user

The code also passed `pycodestyle`.
