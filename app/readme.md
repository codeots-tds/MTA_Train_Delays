1st level:
- list of entities (different api calls made by train)


2nd Level:
- id
- trip_update
- vehicle (sometimes)

3nd level:
- trip dict
- stop_time_update
- current stop sequence
- timestamp
- stop id

4th level
- trip_id
- start date
- route id (train name)


5th level:
- arrival dict
- departure dict

6th level:
- arrival time
- departure time
- stop id


Response Specs:
https://gtfs.org/realtime/proto/
============================================================
message TripUpdate {
  // The Trip that this message applies to. There can be at most one
  // TripUpdate entity for each actual trip instance.
  // If there is none, that means there is no prediction information available.
  // It does *not* mean that the trip is progressing according to schedule.}


