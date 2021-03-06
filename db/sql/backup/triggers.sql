CREATE TRIGGER calculate_points_matches_on_update BEFORE UPDATE ON Clubs
    FOR EACH ROW
    BEGIN
        IF NEW.W < 0 THEN
            SET NEW.W = 0;
        END IF;
        IF NEW.D < 0 THEN
            SET NEW.D = 0;
        END IF;
        IF NEW.L < 0 THEN
            SET NEW.L = 0;
        END IF;
        SET NEW.matches_played = NEW.W + NEW.D + NEW.L;
        SET NEW.points = NEW.W * 3 + NEW.D;
    END;

CREATE TRIGGER calculate_points_matches_on_insert BEFORE INSERT ON Clubs
    FOR EACH ROW
    BEGIN
        IF NEW.W < 0 THEN
            SET NEW.W = 0;
        END IF;
        IF NEW.D < 0 THEN
            SET NEW.D = 0;
        END IF;
        IF NEW.L < 0 THEN
            SET NEW.L = 0;
        END IF;
        SET NEW.points = NEW.W*3 + NEW.D;
        SET NEW.matches_played = NEW.W + NEW.D + NEW.L;
    END;

CREATE TRIGGER check_shirt_number_input BEFORE INSERT ON Players
    FOR EACH ROW
    BEGIN
        IF NEW.number < 0 THEN
            SET NEW.number = 0;
        END IF;
    END;