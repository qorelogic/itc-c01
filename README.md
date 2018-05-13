
Installation:
run ./install.sh


API Endpoints:

```
<Movies API "http://45.63.13.231:8000/docs/">
    : {
        list()
    }
    movie: {
        list()
        create(title, [releaseYear], [casting], [directors], [producers])
        read(id)
        update(id, title, [releaseYear], [casting], [directors], [producers])
        partial_update(id, [title], [releaseYear], [casting], [directors], [producers])
        delete(id)
    }
    person: {
        list()
        create(firstName, [lastName], [aliases], [moviesAsActorActress], [moviesAsDirector], [moviesAsProducer])
        read(id)
        update(id, firstName, [lastName], [aliases], [moviesAsActorActress], [moviesAsDirector], [moviesAsProducer])
        partial_update(id, [firstName], [lastName], [aliases], [moviesAsActorActress], [moviesAsDirector], [moviesAsProducer])
        delete(id)
    }
    users: {
        list()
        create(username, password, [first_name], [last_name], [email])
        read(id)
        update(id, username, password, [first_name], [last_name], [email])
        partial_update(id, [username], [password], [first_name], [last_name], [email])
        delete(id)
    }
```
