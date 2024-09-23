
This file contains the test cases for Dut.py file
"""
import pytest
from Sonnen_task.src.Dut import DUT ,choose_action


class TestEnergyManagement:
    @pytest.fixture
    def dut(self):
        return DUT()


    @pytest.mark.parametrize("pv_production, house_consumption, expected_action",[
                              (10, 5, "Charge with Surplus"),
                              (5,10,"Storge will supply house with power"),
                              (5,5,"Nothing"),
                              (0,0,"Nothing"),
                              (30,15,"Charge with Surplus"),
                              (10,20,"Storge will supply house with power")
                             ])


    def test_energy_management(self, dut, pv_production, house_consumption, expected_action):
        dut.set("pv_production",pv_production)
        dut.set("house_consumption",house_consumption)
        action = choose_action(dut.get("pv_production"),dut.get("house_consumption"))

        assert action == expected_action


    @pytest.mark.parametrize("pv_production,house_consumption",[(10,5),
        (5,10),
        (5,5),
        (0,0),
        (-5,5),
        (5,-5)])


    def test_invalid_inputs(self,dut,pv_production, house_consumption):
        if pv_production  < 0 or house_consumption < 0:
            with pytest.raises(ValueError):
                dut.set("pv_production", pv_production)
                dut.set("house_consumption", house_consumption)
        else:
            dut.set("pv_production", pv_production)
            dut.set("house_consumption", house_consumption)
            action = choose_action(dut.get("pv_production"),dut.get("house_consumption"))
            assert action in ["Charge with Surplus","Storge will supply house with power","Nothing"]

      
