INSERT INTO datausers (user_id, user_name)
VALUES (1234567, 'Boris') ON CONFLICT (user_id) DO UPDATE SET user_name='Boris'