import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

ARN                    = config.get("IAM_ROLE", "ARN")
LOG_DATA               = config.get("S3", "LOG_DATA")
LOG_JSONPATH           = config.get("S3", "LOG_JSONPATH")
SONG_DATA              = config.get("S3", "SONG_DATA")

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events;"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs;"
songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

staging_events_table_create= "CREATE TABLE staging_events \
                                ( \
                                    artist varchar, \
                                    auth varchar, \
                                    firstName varchar, \
                                    gender char, \
                                    itemInSession integer, \
                                    lastName varchar, \
                                    length float, \
                                    level varchar, \
                                    location varchar, \
                                    method varchar, \
                                    page varchar, \
                                    registration varchar, \
                                    sessionId int NOT NULL SORTKEY DISTKEY, \
                                    song varchar, \
                                    status int, \
                                    ts bigint NOT NULL, \
                                    userAgent varchar, \
                                    userId int \
                                );"
                             
staging_songs_table_create = "CREATE TABLE staging_songs \
                                 ( \
                                     num_songs int, \
                                     artist_id varchar NOT NULL SORTKEY DISTKEY, \
                                     artist_latitude float, \
                                     artist_longitude float, \
                                     artist_location varchar, \
                                     artist_name varchar, \
                                     song_id varchar NOT NULL, \
                                     title varchar, \
                                     duration float, \
                                     year int \
                                );"
                              
songplay_table_create = "CREATE TABLE songplays \
                            ( \
                                songplay_id int IDENTITY(0,1) NOT NULL SORTKEY, \
                                start_time timestamp, \
                                user_id int NOT NULL DISTKEY, \
                                level varchar, \
                                song_id varchar, \
                                artist_id varchar, \
                                session_id int, \
                                location varchar, \
                                useragent varchar \
                            );"


user_table_create = "CREATE TABLE users \
                        ( \
                            user_id int NOT NULL SORTKEY, \
                            first_name varchar, \
                            last_name varchar, \
                            gender char, \
                            level varchar \
                        ) \
                        diststyle all;"

song_table_create = "CREATE TABLE songs \
                        ( \
                            song_id varchar NOT NULL SORTKEY, \
                            title varchar NOT NULL, \
                            artist_id varchar NOT NULL, \
                            year int NOT NULL, \
                            duration float NOT NULL \
                        );"

artist_table_create = "CREATE TABLE artists \
                        ( \
                            artist_id varchar NOT NULL SORTKEY, \
                            name varchar, \
                            location varchar, \
                            latitude float, \
                            longitude float \
                        ) \
                        diststyle all;"

time_table_create = "CREATE TABLE time \
                        ( \
                            start_time timestamp NOT NULL SORTKEY, \
                            hour int, \
                            day int, \
                            week int, \
                            month int, \
                            year int, \
                            weekday int \
                        ) \
                        diststyle all;"
                    

# STAGING TABLES

staging_events_copy = ("""COPY staging_events FROM {} IAM_ROLE {} JSON {}""").format(LOG_DATA,ARN,LOG_JSONPATH)

staging_songs_copy = ("""COPY staging_songs FROM {} IAM_ROLE {} JSON 'auto'""").format(SONG_DATA,ARN)

# FINAL TABLES

songplay_table_insert = "INSERT INTO songplays \
                            (  start_time, \
                               user_id, \
                               level, \
                               song_id, \
                               artist_id, \
                               session_id, \
                               location, \
                               useragent \
                            ) \
                          SELECT  distinct \
                                TIMESTAMP 'epoch' + ts/1000 * interval '1 second' , \
                                userid, \
                                level, \
                                song_id, \
                                artist_id, \
                                sessionid, \
                                location, \
                                useragent \
                          FROM staging_events e \
                          JOIN staging_songs s\
                          ON e.artist=s.artist_name \
                          WHERE page='NextSong' ;\
                        "

user_table_insert = "INSERT INTO users \
                        SELECT DISTINCT \
                            userid, firstname, lastname, gender, level \
                        FROM staging_events \
                        WHERE page='NextSong'; \
                     "                    

song_table_insert = "INSERT INTO songs \
                        SELECT DISTINCT \
                            song_id, \
                            title, \
                            artist_id, \
                            year, \
                            duration \
                        FROM staging_songs; \
                    "

artist_table_insert = "INSERT INTO artists \
                            SELECT DISTINCT \
                                artist_id, \
                                artist_name, \
                                artist_location, \
                                artist_latitude, \
                                artist_longitude \
                            FROM staging_songs; \
                       "

time_table_insert = "INSERT INTO time \
                        SELECT DISTINCT \
                            TIMESTAMP 'epoch' + ts/1000 * interval '1 second' AS start_time ,  \
                            EXTRACT (hour FROM start_time) , \
                            EXTRACT(day FROM start_time)   , \
                            EXTRACT(week FROM start_time)  , \
                            EXTRACT(month FROM start_time) , \
                            EXTRACT(year FROM start_time)  , \
                            EXTRACT(weekday FROM start_time)  \
                        FROM staging_events \
                     where page='NextSong' ; \
                    "

# QUERY LISTS

drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]

copy_table_queries = [staging_events_copy, staging_songs_copy]

insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
