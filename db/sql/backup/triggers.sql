CREATE TRIGGER calculate_points_matches_on_update BEFORE UPDATE ON Clubs
    FOR EACH ROW
    BEGIN
        IF NEW.W < 0 THEN
            SET NEW.W = 0;
        ELSEIF NEW.D < 0 THEN
            SET NEW.D = 0;
        ELSEIF NEW.L < 0 THEN
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
        ELSEIF NEW.D < 0 THEN
            SET NEW.D = 0;
        ELSEIF NEW.L < 0 THEN
            SET NEW.L = 0;
        END IF;
        SET NEW.points = NEW.W*3 + NEW.D;
        SET NEW.matches_played = NEW.W + NEW.D + NEW.L;
    END;