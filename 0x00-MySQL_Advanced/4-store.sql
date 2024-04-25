-- creates a trigger that decreases the number of an item
-- after adding a new one
DELIMITER //
CREATE TRIGGER decrease_quantity_trigger
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END;
//
DELIMITER ;
