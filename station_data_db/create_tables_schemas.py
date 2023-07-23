
create_subway_station_table = """

CREATE TABLE IF NOT EXISTS subway_station_table(
      stop_id VARCHAR(10),
      complex_id INT,
      division VARCHAR(8),
      line VARCHAR(50),
      station_name VARCHAR(80),
      borough VARCHAR(10),
      trains VARCHAR(40),
      structure VARCHAR(50),
      latitude FLOAT,
      longitude FLOAT,
      north_direction_label VARCHAR(80),
      south_direction_label VARCHAR(80),
      station_id INT,
      PRIMARY KEY (stop_id)
)"""

#mta subway delays data. updated frequently and stores data upto a week.
#week just might be the date_beginning_of_week and date_end_of_week
create_subway_delays_table = """
CREATE TABLE IF NOT EXISTS subway_delays_table(
      subway_train VARCHAR(10),
      num_of_delays VARCHAR(10),
      date VARCHAR(10),
"""

create_tables = [create_subway_station_table]
