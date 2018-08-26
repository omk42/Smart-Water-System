from water_system import Water_System

if __name__ == "__main__":
    water_system_obj = Water_System()
    try:
        water_system_obj.run()
    finally:
        water_system_obj.pi_cleanup()