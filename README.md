# Nokia-WebApp-UPT

It's a web application built in Python with Django.

The main functionality of the application is to read information about Nokia's tests, from notepad, extract them, filter them, group them and make calculations based on them.

In order to use the application, you need to register an account. When you logged in, you can see all the tests, all of them being grouped by their special id. When you go on a test, you can see the passed and failed ones and the percentage of the passed ones.
You can also add some category tests to your favorite list so it will be easier to check them.

A cool feature is that if the notepads are being edited, so the tests will change, we can turn on Celery Beat, which is a scheduler, so it will do a periodic task every time we want to, in order to update the new tests.

