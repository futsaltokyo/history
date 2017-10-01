CREATE TABLE IF NOT EXISTS events (
  id BIGINT PRIMARY KEY,
  name TEXT NOT NULL,
  created TIMESTAMP,
  duration INTEGER,
  rsvp_limit SMALLINT,
  started TIMESTAMP,
  venue_id BIGINT NOT NULL,
  fee NUMERIC(10, 4) NOT NULL DEFAULT 0,
  currency CHAR(3) NOT NULL DEFAULT 'JPY'
);

CREATE INDEX IF NOT EXISTS events_started_idx ON events(started);
CREATE INDEX IF NOT EXISTS events_venue_id_idx ON events(venue_id);

CREATE TABLE IF NOT EXISTS members (
  id BIGINT PRIMARY KEY,
  name TEXT NOT NULL,
  image_url TEXT
);

CREATE TABLE IF NOT EXISTS attendees (
  event_id BIGINT NOT NULL REFERENCES events(id),
  member_id BIGINT NOT NULL REFERENCES members(id),

  PRIMARY KEY (event_id, member_id)
);

CREATE INDEX IF NOT EXISTS attendees_member_id_idx ON attendees(member_id);
