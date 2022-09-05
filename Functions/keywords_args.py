def describe_pet(animal_typed, pet_name):
    """Dispaly information about a pet"""
    print("\nI have a "+animal_typed+".")
    print("My "+animal_typed+"'s name is "+pet_name.title()+".")


# keywords arguments
describe_pet(animal_typed='hamster', pet_name='harry')
