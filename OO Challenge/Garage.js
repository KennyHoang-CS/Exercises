class Garage{
    constructor(capacity){
        this.capacity = capacity;
        this.vehicles = [];
    }
    add(newVehicle){
        
        if(!(newVehicle instanceof Vehicle)){
            return 'Only vehicles are allowed in here!';
        }
        if(this.vehicles.length >= this.capacity){
            return `Sorry, we're full.`;
        }
        this.vehicles.push(newVehicle);
        return 'Vehicle added!';
    }
}