"""Recycled Paper solution model.
   Excel filename: Drawdown-Recycled Paper_RRS_v1.1_17Nov2018_PUBLIC.xlsm
"""

import pathlib

import numpy as np
import pandas as pd

from model import adoptiondata
from model import advanced_controls
from model import ch4calcs
from model import co2calcs
from model import customadoption
from model import emissionsfactors
from model import firstcost
from model import helpertables
from model import operatingcost
from model import s_curve
from model import unitadoption
from model import vma
from model.advanced_controls import SOLUTION_CATEGORY

from model import tam
from solution import rrs

DATADIR = str(pathlib.Path(__file__).parents[2].joinpath('data'))
THISDIR = pathlib.Path(__file__).parents[0]
REGIONS = ['World', 'OECD90', 'Eastern Europe', 'Asia (Sans Japan)', 'Middle East and Africa',
           'Latin America', 'China', 'India', 'EU', 'USA']

scenarios = {
  'PDS1-67p2050-Low Growth (Book Ed.1)': advanced_controls.AdvancedControls(
      # The growth of adoption is based on low (1 standard deviation below the mean
      # annual) values of adoption from existing prognostications from the literature.
      # No learning rate is assumed. This scenario uses inputs calculated for the
      # Drawdown book edition 1, some of which have been updated.

      # general
      report_start_year=2020, report_end_year=2050, 

      # adoption
      soln_ref_adoption_basis='Default', 
      soln_ref_adoption_regional_data=False, soln_pds_adoption_regional_data=False, 
      soln_pds_adoption_basis='Existing Adoption Prognostications', 
      soln_pds_adoption_prognostication_source='ALL SOURCES', 
      soln_pds_adoption_prognostication_trend='3rd Poly', 
      soln_pds_adoption_prognostication_growth='Low', 
      source_until_2014='See McKinnsey & Co 2013 sheet (annual growth after 2030 2,7%', 
      ref_source_post_2014='Maximum Cases', 
      pds_source_post_2014='Maximum Cases', 
      pds_adoption_final_percentage=[('World', 0.0), ('OECD90', 0.0), ('Eastern Europe', 0.0), ('Asia (Sans Japan)', 0.0), ('Middle East and Africa', 0.0), ('Latin America', 0.0), ('China', 0.0), ('India', 0.0), ('EU', 0.0), ('USA', 0.0)], 

      # financial
      pds_2014_cost=2024020321.786245, ref_2014_cost=2024020321.786245, 
      conv_2014_cost=1505666896.630999, 
      soln_first_cost_efficiency_rate=0.0, 
      conv_first_cost_efficiency_rate=0.0, 
      soln_first_cost_below_conv=True, 
      npv_discount_rate=0.094, 
      soln_lifetime_capacity=1.0, soln_avg_annual_use=1.0, 
      conv_lifetime_capacity=1.0, conv_avg_annual_use=1.0, 

      soln_var_oper_cost_per_funit=0.0, soln_fuel_cost_per_funit=0.0, 
      soln_fixed_oper_cost_per_iunit=0.0, 
      conv_var_oper_cost_per_funit=0.0, conv_fuel_cost_per_funit=0.0, 
      conv_fixed_oper_cost_per_iunit=0.0, 

      # emissions
      ch4_is_co2eq=False, n2o_is_co2eq=False, 
      co2eq_conversion_source='AR5 with feedback', 
      soln_indirect_co2_per_iunit=188839.77976666667, 
      conv_indirect_co2_per_unit=524550.4702999999, 
      conv_indirect_co2_is_iunits=False, 
      ch4_co2_per_twh=0.0, n2o_co2_per_twh=0.0, 

      soln_energy_efficiency_factor=0.0, 
      soln_annual_energy_used=0.0, conv_annual_energy_used=0.0, 
      conv_fuel_consumed_per_funit=0.0, soln_fuel_efficiency_factor=0.0, 
      conv_fuel_emissions_factor=0.0, soln_fuel_emissions_factor=0.0, 

      emissions_grid_source='Meta-Analysis', emissions_grid_range='Mean', 
      emissions_use_co2eq=True, 
      conv_emissions_per_funit=1318973.9612408415, soln_emissions_per_funit=1230043.9188259256, 


      # sequestration
    ),
  'PDS2-77p2050-Mean Growth (Book Ed.1)': advanced_controls.AdvancedControls(
      # The growth of adoption is based on medium values of adoption from existing
      # prognostications from the literature. At later years, restrictions on feedstock
      # due to integration with other Drawdown solutions reduces demand from this trend
      # however. A 14.9% solution learning rate is assumed. This scenario uses inputs
      # calculated for the Drawdown book edition 1, some of which have been updated.

      # general
      report_start_year=2020, report_end_year=2050, 

      # adoption
      soln_ref_adoption_basis='Default', 
      soln_ref_adoption_regional_data=False, soln_pds_adoption_regional_data=False, 
      soln_pds_adoption_basis='Fully Customized PDS', 
      soln_pds_adoption_custom_name='Custom Scenario No.1 - Using Medium Trend of Prognostications', 
      source_until_2014='See McKinnsey & Co 2013 sheet (annual growth after 2030 2,7%', 
      ref_source_post_2014='Maximum Cases', 
      pds_source_post_2014='Maximum Cases', 
      pds_adoption_final_percentage=[('World', 0.0), ('OECD90', 0.0), ('Eastern Europe', 0.0), ('Asia (Sans Japan)', 0.0), ('Middle East and Africa', 0.0), ('Latin America', 0.0), ('China', 0.0), ('India', 0.0), ('EU', 0.0), ('USA', 0.0)], 

      # financial
      pds_2014_cost=2024020321.786245, ref_2014_cost=2024020321.786245, 
      conv_2014_cost=1505666896.630999, 
      soln_first_cost_efficiency_rate=0.149, 
      conv_first_cost_efficiency_rate=0.0, 
      soln_first_cost_below_conv=True, 
      npv_discount_rate=0.094, 
      soln_lifetime_capacity=1.0, soln_avg_annual_use=1.0, 
      conv_lifetime_capacity=1.0, conv_avg_annual_use=1.0, 

      soln_var_oper_cost_per_funit=0.0, soln_fuel_cost_per_funit=0.0, 
      soln_fixed_oper_cost_per_iunit=0.0, 
      conv_var_oper_cost_per_funit=0.0, conv_fuel_cost_per_funit=0.0, 
      conv_fixed_oper_cost_per_iunit=0.0, 

      # emissions
      ch4_is_co2eq=False, n2o_is_co2eq=False, 
      co2eq_conversion_source='AR5 with feedback', 
      soln_indirect_co2_per_iunit=188839.77976666667, 
      conv_indirect_co2_per_unit=524550.4702999999, 
      conv_indirect_co2_is_iunits=False, 
      ch4_co2_per_twh=0.0, n2o_co2_per_twh=0.0, 

      soln_energy_efficiency_factor=0.0, 
      soln_annual_energy_used=0.0, conv_annual_energy_used=0.0, 
      conv_fuel_consumed_per_funit=0.0, soln_fuel_efficiency_factor=0.0, 
      conv_fuel_emissions_factor=0.0, soln_fuel_emissions_factor=0.0, 

      emissions_grid_source='Meta-Analysis', emissions_grid_range='Mean', 
      emissions_use_co2eq=True, 
      conv_emissions_per_funit=1318973.9612408415, soln_emissions_per_funit=1230043.9188259256, 


      # sequestration
    ),
  'PDS3-80p2050-High Growth (Book Ed.1)': advanced_controls.AdvancedControls(
      # The growth of adoption is based on high values of adoption from existing
      # prognostications from the literature. At later years, restrictions on feedstock
      # due to integration with other Drawdown solutions reduces demand from this trend
      # however. A 14.9% solution learning rate is assumed. This scenario uses inputs
      # calculated for the Drawdown book edition 1, some of which have been updated.

      # general
      report_start_year=2020, report_end_year=2050, 

      # adoption
      soln_ref_adoption_basis='Default', 
      soln_ref_adoption_regional_data=False, soln_pds_adoption_regional_data=False, 
      soln_pds_adoption_basis='Fully Customized PDS', 
      soln_pds_adoption_custom_name='Custom Scenario No.2 - Using High Trend of Existing Prognostications', 
      source_until_2014='See McKinnsey & Co 2013 sheet (annual growth after 2030 2,7%', 
      ref_source_post_2014='Maximum Cases', 
      pds_source_post_2014='Maximum Cases', 
      pds_adoption_final_percentage=[('World', 0.0), ('OECD90', 0.0), ('Eastern Europe', 0.0), ('Asia (Sans Japan)', 0.0), ('Middle East and Africa', 0.0), ('Latin America', 0.0), ('China', 0.0), ('India', 0.0), ('EU', 0.0), ('USA', 0.0)], 

      # financial
      pds_2014_cost=2024020321.786245, ref_2014_cost=2024020321.786245, 
      conv_2014_cost=1505666896.630999, 
      soln_first_cost_efficiency_rate=0.149, 
      conv_first_cost_efficiency_rate=0.0, 
      soln_first_cost_below_conv=True, 
      npv_discount_rate=0.094, 
      soln_lifetime_capacity=1.0, soln_avg_annual_use=1.0, 
      conv_lifetime_capacity=1.0, conv_avg_annual_use=1.0, 

      soln_var_oper_cost_per_funit=0.0, soln_fuel_cost_per_funit=0.0, 
      soln_fixed_oper_cost_per_iunit=0.0, 
      conv_var_oper_cost_per_funit=0.0, conv_fuel_cost_per_funit=0.0, 
      conv_fixed_oper_cost_per_iunit=0.0, 

      # emissions
      ch4_is_co2eq=False, n2o_is_co2eq=False, 
      co2eq_conversion_source='AR5 with feedback', 
      soln_indirect_co2_per_iunit=188839.77976666667, 
      conv_indirect_co2_per_unit=524550.4702999999, 
      conv_indirect_co2_is_iunits=False, 
      ch4_co2_per_twh=0.0, n2o_co2_per_twh=0.0, 

      soln_energy_efficiency_factor=0.0, 
      soln_annual_energy_used=0.0, conv_annual_energy_used=0.0, 
      conv_fuel_consumed_per_funit=0.0, soln_fuel_efficiency_factor=0.0, 
      conv_fuel_emissions_factor=0.0, soln_fuel_emissions_factor=0.0, 

      emissions_grid_source='Meta-Analysis', emissions_grid_range='Mean', 
      emissions_use_co2eq=True, 
      conv_emissions_per_funit=1318973.9612408415, soln_emissions_per_funit=1230043.9188259256, 


      # sequestration
    ),
}

class RecycledPaper:
  name = 'Recycled Paper'
  units = {
    "implementation unit": "Million Metric Tonnes of Recycled Paper Produced",
    "functional unit": "Million Metric Tonnes of Paper Produced",
    "first cost": "US$B",
    "operating cost": "US$B",
  }

  def __init__(self, scenario=None):
    if scenario is None:
      scenario = 'PDS1-67p2050-Low Growth (Book Ed.1)'
    self.scenario = scenario
    self.ac = scenarios[scenario]

    # TAM
    tamconfig_list = [
      ['param', 'World', 'PDS World', 'OECD90', 'Eastern Europe', 'Asia (Sans Japan)',
       'Middle East and Africa', 'Latin America', 'China', 'India', 'EU', 'USA'],
      ['source_until_2014', self.ac.source_until_2014, self.ac.source_until_2014,
       'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES',
       'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES'],
      ['source_after_2014', self.ac.ref_source_post_2014, self.ac.pds_source_post_2014,
       'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES',
       'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES'],
      ['trend', '3rd Poly', '3rd Poly',
       '3rd Poly', '3rd Poly', '3rd Poly', '3rd Poly', '3rd Poly', '3rd Poly',
       '3rd Poly', '3rd Poly', '2nd Poly'],
      ['growth', 'Medium', 'Medium', 'Medium', 'Medium',
       'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium'],
      ['low_sd_mult', 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      ['high_sd_mult', 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]]
    tamconfig = pd.DataFrame(tamconfig_list[1:], columns=tamconfig_list[0], dtype=np.object).set_index('param')
    tam_ref_data_sources = {
      'Baseline Cases': {
          '[FAO Stat 2014] Original data from webpage FAO Stat 2014. See RIGI data on the same sheet for annual growth rates in Drawdown regions (2015-2020, 2020-2030 and 2030-2045).': THISDIR.joinpath('tam_FAO_Stat_2014_Original_data_from_webpage_FAO_Stat_2014__See_RIGedf64645.csv'),
          'See sheet FAO 2009, annual growth rates in Drawdown regions (2015-2020, 2020-2030 and 2030-2045) from RISI': THISDIR.joinpath('tam_See_sheet_FAO_2009_annual_growth_rates_in_Drawdown_regions_2015489d056e.csv'),
      },
      'Ambitious Cases': {
          'See McKinnsey & Co 2013 sheet (annual growth after 2030 2,7%': THISDIR.joinpath('tam_See_McKinnsey_Co_2013_sheet_annual_growth_after_2030_27.csv'),
      },
      'Maximum Cases': {
          'See McKinnsey & Co 2013 sheet (annual growth after 2030 2,2%': THISDIR.joinpath('tam_See_McKinnsey_Co_2013_sheet_annual_growth_after_2030_22.csv'),
      },
      'Region: OECD90': {
        'Baseline Cases': {
          '[FAO Stat 2014] Original data from webpage FAO Stat 2014. See RIGI data on the same sheet for annual growth rates in Drawdown regions (2015-2020, 2020-2030 and 2030-2045).': THISDIR.joinpath('tam_FAO_Stat_2014_Original_data_from_webpage_FAO_Stat_2014__See_RIGedf64645.csv'),
          'See sheet FAO 2009': THISDIR.joinpath('tam_See_sheet_FAO_2009.csv'),
        },
      },
      'Region: Eastern Europe': {
        'Baseline Cases': {
          '[FAO Stat 2014] Original data from webpage FAO Stat 2014. See RIGI data on the same sheet for annual growth rates in Drawdown regions (2015-2020, 2020-2030 and 2030-2045).': THISDIR.joinpath('tam_FAO_Stat_2014_Original_data_from_webpage_FAO_Stat_2014__See_RIGedf64645.csv'),
          'See sheet FAO 2009': THISDIR.joinpath('tam_See_sheet_FAO_2009.csv'),
        },
      },
      'Region: Asia (Sans Japan)': {
        'Baseline Cases': {
          '[FAO Stat 2014] Original data from webpage FAO Stat 2014. See RIGI data on the same sheet for annual growth rates in Drawdown regions (2015-2020, 2020-2030 and 2030-2045).': THISDIR.joinpath('tam_FAO_Stat_2014_Original_data_from_webpage_FAO_Stat_2014__See_RIGedf64645.csv'),
          'See sheet FAO 2009': THISDIR.joinpath('tam_See_sheet_FAO_2009.csv'),
        },
      },
      'Region: Middle East and Africa': {
        'Baseline Cases': {
          '[FAO Stat 2014] Original data from webpage FAO Stat 2014. See RIGI data on the same sheet for annual growth rates in Drawdown regions (2015-2020, 2020-2030 and 2030-2045).': THISDIR.joinpath('tam_FAO_Stat_2014_Original_data_from_webpage_FAO_Stat_2014__See_RIGedf64645.csv'),
          'See sheet FAO 2009': THISDIR.joinpath('tam_See_sheet_FAO_2009.csv'),
        },
      },
      'Region: Latin America': {
        'Baseline Cases': {
          '[FAO Stat 2014] Original data from webpage FAO Stat 2014. See RIGI data on the same sheet for annual growth rates in Drawdown regions (2015-2020, 2020-2030 and 2030-2045).': THISDIR.joinpath('tam_FAO_Stat_2014_Original_data_from_webpage_FAO_Stat_2014__See_RIGedf64645.csv'),
          'See sheet FAO 2009': THISDIR.joinpath('tam_See_sheet_FAO_2009.csv'),
        },
      },
      'Region: China': {
        'Baseline Cases': {
          '[FAO Stat 2014] Original data from webpage FAO Stat 2014. See RIGI data on the same sheet for annual growth rates in Drawdown regions and countries (2015-2020, 2020-2030 and 2030-2045).': THISDIR.joinpath('tam_FAO_Stat_2014_Original_data_from_webpage_FAO_Stat_2014__See_RIG26cb163b.csv'),
        },
        'Ambitious Cases': {
          'See sheet PÖYRY 2013. Linear interpolation 2011-2025 is used. After 2025 annual growth rate of 3,6% is used according to FAO 2009 Asia and the Pacific region annual growth rate 2020-2030.': THISDIR.joinpath('tam_See_sheet_PÖYRY_2013__Linear_interpolation_20112025_is_used__Afc4cf2831.csv'),
        },
      },
      'Region: India': {
        'Baseline Cases': {
          '[FAO Stat 2014] Original data from webpage FAO Stat 2014. See RIGI data on the same sheet for annual growth rates in Drawdown regions and countries (2015-2020, 2020-2030 and 2030-2045).': THISDIR.joinpath('tam_FAO_Stat_2014_Original_data_from_webpage_FAO_Stat_2014__See_RIG26cb163b.csv'),
        },
      },
      'Region: EU': {
        'Baseline Cases': {
          '[FAO Stat 2014] Original data from webpage FAO Stat 2014. See RIGI data on the same sheet for annual growth rates in Drawdown regions and countries (2015-2020, 2020-2030 and 2030-2045).': THISDIR.joinpath('tam_FAO_Stat_2014_Original_data_from_webpage_FAO_Stat_2014__See_RIG26cb163b.csv'),
        },
      },
      'Region: USA': {
        'Baseline Cases': {
          '[FAO Stat 2014] Original data from webpage FAO Stat 2014. See RIGI data on the same sheet for annual growth rates in Drawdown regions and countries (2015-2020, 2020-2030 and 2030-2045).': THISDIR.joinpath('tam_FAO_Stat_2014_Original_data_from_webpage_FAO_Stat_2014__See_RIG26cb163b.csv'),
          'See sheet FAO 2015-2020, prognostication based on RIGI -0.9% annum growth': THISDIR.joinpath('tam_See_sheet_FAO_20152020_prognostication_based_on_RIGI_0_9_annum_739b4dc6.csv'),
        },
      },
    }
    self.tm = tam.TAM(tamconfig=tamconfig, tam_ref_data_sources=tam_ref_data_sources,
      world_includes_regional=True,
      tam_pds_data_sources=tam_ref_data_sources)
    ref_tam_per_region=self.tm.ref_tam_per_region()
    pds_tam_per_region=self.tm.pds_tam_per_region()

    adconfig_list = [
      ['param', 'World', 'OECD90', 'Eastern Europe', 'Asia (Sans Japan)',
       'Middle East and Africa', 'Latin America', 'China', 'India', 'EU', 'USA'],
      ['trend', self.ac.soln_pds_adoption_prognostication_trend, '3rd Poly',
       '3rd Poly', '3rd Poly', '3rd Poly', '3rd Poly', '3rd Poly',
       '3rd Poly', '3rd Poly', '3rd Poly'],
      ['growth', self.ac.soln_pds_adoption_prognostication_growth, 'Medium',
       'Medium', 'Medium', 'Medium', 'Medium', 'Medium',
       'Medium', 'Medium', 'Medium'],
      ['low_sd_mult', 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      ['high_sd_mult', 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]]
    adconfig = pd.DataFrame(adconfig_list[1:], columns=adconfig_list[0], dtype=np.object).set_index('param')
    ad_data_sources = {
      'Baseline Cases': {
          'See sheet FAO Stat 2014, recycling target rates specially defined for each region and country based on current recycling rate and EU target 2030 recycling rate of 70% or closest best country/region recycling rate': THISDIR.joinpath('ad_See_sheet_FAO_Stat_2014_recycling_target_rates_specially_definec0952f24.csv'),
      },
      'Conservative Cases': {
          'See PÖYRY 2013 sheet': THISDIR.joinpath('ad_See_PÖYRY_2013_sheet.csv'),
          'See McKinsey and Co. 2013 (adoption doubles every 25 years), 3rd Polynomial prognostication': THISDIR.joinpath('ad_See_McKinsey_and_Co__2013_adoption_doubles_every_25_years_3rd_Pbc48626a.csv'),
      },
      'Ambitious Cases': {
          'Sheet FAO Stat 2014, ceiling 75%': THISDIR.joinpath('ad_Sheet_FAO_Stat_2014_ceiling_75.csv'),
      },
      'Maximum Cases': {
          'Sheet FAO Stat 2014, ceiling 81%': THISDIR.joinpath('ad_Sheet_FAO_Stat_2014_ceiling_81.csv'),
          'See McKinsey and Co. 2013 (adoption doubles every 15 years), 3rd Polynomial prognostication': THISDIR.joinpath('ad_See_McKinsey_and_Co__2013_adoption_doubles_every_15_years_3rd_Pbc48626a.csv'),
      },
      'Region: OECD90': {
        'Baseline Cases': {
          'See sheet FAO Stat 2014, recycling target rates specially defined for each region and country based on current recycling rate and EU target 2030 recycling rate of 70% or closest best country/region recycling rate': THISDIR.joinpath('ad_See_sheet_FAO_Stat_2014_recycling_target_rates_specially_definec0952f24.csv'),
        },
        'Ambitious Cases': {
          'Sheet FAO Stat 2014, ceiling 75%': THISDIR.joinpath('ad_Sheet_FAO_Stat_2014_ceiling_75.csv'),
        },
        'Maximum Cases': {
          'Sheet FAO Stat 2014, ceiling 81%': THISDIR.joinpath('ad_Sheet_FAO_Stat_2014_ceiling_81.csv'),
        },
      },
      'Region: Eastern Europe': {
        'Baseline Cases': {
          'See sheet FAO Stat 2014, recycling target rates specially defined for each region and country based on current recycling rate and EU target 2030 recycling rate of 70% or closest best country/region recycling rate': THISDIR.joinpath('ad_See_sheet_FAO_Stat_2014_recycling_target_rates_specially_definec0952f24.csv'),
        },
        'Ambitious Cases': {
          'Sheet FAO Stat 2014, ceiling 75%': THISDIR.joinpath('ad_Sheet_FAO_Stat_2014_ceiling_75.csv'),
        },
        'Maximum Cases': {
          'Sheet FAO Stat 2014, ceiling 81%': THISDIR.joinpath('ad_Sheet_FAO_Stat_2014_ceiling_81.csv'),
        },
      },
      'Region: Asia (Sans Japan)': {
        'Baseline Cases': {
          'See sheet FAO Stat 2014, recycling target rates specially defined for each region and country based on current recycling rate and EU target 2030 recycling rate of 70% or closest best country/region recycling rate': THISDIR.joinpath('ad_See_sheet_FAO_Stat_2014_recycling_target_rates_specially_definec0952f24.csv'),
        },
        'Ambitious Cases': {
          'Sheet FAO Stat 2014, ceiling 75%': THISDIR.joinpath('ad_Sheet_FAO_Stat_2014_ceiling_75.csv'),
        },
        'Maximum Cases': {
          'Sheet FAO Stat 2014, ceiling 81%': THISDIR.joinpath('ad_Sheet_FAO_Stat_2014_ceiling_81.csv'),
        },
      },
      'Region: Middle East and Africa': {
        'Baseline Cases': {
          'See sheet FAO Stat 2014, recycling target rates specially defined for each region and country based on current recycling rate and EU target 2030 recycling rate of 70% or closest best country/region recycling rate': THISDIR.joinpath('ad_See_sheet_FAO_Stat_2014_recycling_target_rates_specially_definec0952f24.csv'),
        },
        'Ambitious Cases': {
          'Sheet FAO Stat 2014, ceiling 75%': THISDIR.joinpath('ad_Sheet_FAO_Stat_2014_ceiling_75.csv'),
        },
        'Maximum Cases': {
          'Sheet FAO Stat 2014, ceiling 81%': THISDIR.joinpath('ad_Sheet_FAO_Stat_2014_ceiling_81.csv'),
        },
      },
      'Region: Latin America': {
        'Baseline Cases': {
          'See sheet FAO Stat 2014, recycling target rates specially defined for each region and country based on current recycling rate and EU target 2030 recycling rate of 70% or closest best country/region recycling rate': THISDIR.joinpath('ad_See_sheet_FAO_Stat_2014_recycling_target_rates_specially_definec0952f24.csv'),
        },
        'Ambitious Cases': {
          'Sheet FAO Stat 2014, ceiling 75%': THISDIR.joinpath('ad_Sheet_FAO_Stat_2014_ceiling_75.csv'),
        },
        'Maximum Cases': {
          'Sheet FAO Stat 2014, ceiling 81%': THISDIR.joinpath('ad_Sheet_FAO_Stat_2014_ceiling_81.csv'),
        },
      },
      'Region: China': {
        'Baseline Cases': {
          'See sheet FAO Stat 2014, recycling target rates specially defined for each region and country based on current recycling rate and EU target 2030 recycling rate of 70% or closest best country/region recycling rate': THISDIR.joinpath('ad_See_sheet_FAO_Stat_2014_recycling_target_rates_specially_definec0952f24.csv'),
        },
        'Ambitious Cases': {
          'Sheet FAO Stat 2014, ceiling 75%': THISDIR.joinpath('ad_Sheet_FAO_Stat_2014_ceiling_75.csv'),
        },
        'Maximum Cases': {
          'Sheet FAO Stat 2014, ceiling 81%': THISDIR.joinpath('ad_Sheet_FAO_Stat_2014_ceiling_81.csv'),
        },
      },
      'Region: India': {
        'Baseline Cases': {
          'See sheet FAO Stat 2014, recycling target rates specially defined for each region and country based on current recycling rate and EU target 2030 recycling rate of 70% or closest best country/region recycling rate': THISDIR.joinpath('ad_See_sheet_FAO_Stat_2014_recycling_target_rates_specially_definec0952f24.csv'),
        },
        'Ambitious Cases': {
          'Sheet FAO Stat 2014, ceiling 75%': THISDIR.joinpath('ad_Sheet_FAO_Stat_2014_ceiling_75.csv'),
        },
        'Maximum Cases': {
          'Sheet FAO Stat 2014, ceiling 81%': THISDIR.joinpath('ad_Sheet_FAO_Stat_2014_ceiling_81.csv'),
        },
      },
      'Region: EU': {
        'Baseline Cases': {
          'See sheet FAO Stat 2014, recycling target rates specially defined for each region and country based on current recycling rate and EU target 2030 recycling rate of 70% or closest best country/region recycling rate': THISDIR.joinpath('ad_See_sheet_FAO_Stat_2014_recycling_target_rates_specially_definec0952f24.csv'),
        },
        'Ambitious Cases': {
          'Sheet FAO Stat 2014, ceiling 75%': THISDIR.joinpath('ad_Sheet_FAO_Stat_2014_ceiling_75.csv'),
        },
        'Maximum Cases': {
          'Sheet FAO Stat 2014, ceiling 81%': THISDIR.joinpath('ad_Sheet_FAO_Stat_2014_ceiling_81.csv'),
        },
      },
      'Region: USA': {
        'Baseline Cases': {
          'See sheet FAO Stat 2014, recycling target rates specially defined for each region and country based on current recycling rate and EU target 2030 recycling rate of 70% or closest best country/region recycling rate': THISDIR.joinpath('ad_See_sheet_FAO_Stat_2014_recycling_target_rates_specially_definec0952f24.csv'),
        },
        'Ambitious Cases': {
          'Sheet FAO Stat 2014, ceiling 75%': THISDIR.joinpath('ad_Sheet_FAO_Stat_2014_ceiling_75.csv'),
        },
        'Maximum Cases': {
          'Sheet FAO Stat 2014, ceiling 81%': THISDIR.joinpath('ad_Sheet_FAO_Stat_2014_ceiling_81.csv'),
        },
      },
    }
    self.ad = adoptiondata.AdoptionData(ac=self.ac, data_sources=ad_data_sources,
        adconfig=adconfig)

    # Custom PDS Data
    ca_pds_data_sources = [
      {'name': 'Custom Scenario No.1 - Using Medium Trend of Prognostications', 'include': True,
          'filename': THISDIR.joinpath('ca_pds_data', 'custom_pds_ad_Custom_Scenario_No_1_Using_Medium_Trend_of_Prognostications.csv')},
      {'name': 'Custom Scenario No.2 - Using High Trend of Existing Prognostications', 'include': True,
          'filename': THISDIR.joinpath('ca_pds_data', 'custom_pds_ad_Custom_Scenario_No_2_Using_High_Trend_of_Existing_Prognosticati92e283db.csv')},
    ]
    self.pds_ca = customadoption.CustomAdoption(data_sources=ca_pds_data_sources,
        soln_adoption_custom_name=self.ac.soln_pds_adoption_custom_name,
        high_sd_mult=1.0, low_sd_mult=1.0)

    if False:
      # One may wonder why this is here. This file was code generated.
      # This 'if False' allows subsequent conditions to all be elif.
      pass
    elif self.ac.soln_pds_adoption_basis == 'Fully Customized PDS':
      pds_adoption_data_per_region = self.pds_ca.adoption_data_per_region()
      pds_adoption_trend_per_region = self.pds_ca.adoption_trend_per_region()
      pds_adoption_is_single_source = None
    elif self.ac.soln_pds_adoption_basis == 'Existing Adoption Prognostications':
      pds_adoption_data_per_region = self.ad.adoption_data_per_region()
      pds_adoption_trend_per_region = self.ad.adoption_trend_per_region()
      pds_adoption_is_single_source = self.ad.adoption_is_single_source()

    ht_ref_adoption_initial = pd.Series(
      [207.0, 125.0, 6.3, 78.0, 2.75,
       12.21, 44.0, 3.0, 69.0, 46.5],
       index=REGIONS)
    ht_ref_adoption_final = ref_tam_per_region.loc[2050] * (ht_ref_adoption_initial / ref_tam_per_region.loc[2014])
    ht_ref_datapoints = pd.DataFrame(columns=REGIONS)
    ht_ref_datapoints.loc[2014] = ht_ref_adoption_initial
    ht_ref_datapoints.loc[2050] = ht_ref_adoption_final.fillna(0.0)
    ht_pds_adoption_initial = ht_ref_adoption_initial
    ht_regions, ht_percentages = zip(*self.ac.pds_adoption_final_percentage)
    ht_pds_adoption_final_percentage = pd.Series(list(ht_percentages), index=list(ht_regions))
    ht_pds_adoption_final = ht_pds_adoption_final_percentage * pds_tam_per_region.loc[2050]
    ht_pds_datapoints = pd.DataFrame(columns=REGIONS)
    ht_pds_datapoints.loc[2014] = ht_pds_adoption_initial
    ht_pds_datapoints.loc[2050] = ht_pds_adoption_final.fillna(0.0)
    self.ht = helpertables.HelperTables(ac=self.ac,
                                        ref_datapoints=ht_ref_datapoints, pds_datapoints=ht_pds_datapoints,
                                        pds_adoption_data_per_region=pds_adoption_data_per_region,
                                        ref_adoption_limits=ref_tam_per_region, pds_adoption_limits=pds_tam_per_region,
                                        pds_adoption_trend_per_region=pds_adoption_trend_per_region,
                                        pds_adoption_is_single_source=pds_adoption_is_single_source)

    self.ef = emissionsfactors.ElectricityGenOnGrid(ac=self.ac)

    self.ua = unitadoption.UnitAdoption(ac=self.ac,
        ref_tam_per_region=ref_tam_per_region, pds_tam_per_region=pds_tam_per_region,
        soln_ref_funits_adopted=self.ht.soln_ref_funits_adopted(),
        soln_pds_funits_adopted=self.ht.soln_pds_funits_adopted(),
        bug_cfunits_double_count=True)
    soln_pds_tot_iunits_reqd = self.ua.soln_pds_tot_iunits_reqd()
    soln_ref_tot_iunits_reqd = self.ua.soln_ref_tot_iunits_reqd()
    conv_ref_tot_iunits = self.ua.conv_ref_tot_iunits()
    soln_net_annual_funits_adopted=self.ua.soln_net_annual_funits_adopted()

    self.fc = firstcost.FirstCost(ac=self.ac, pds_learning_increase_mult=2,
        ref_learning_increase_mult=2, conv_learning_increase_mult=2,
        soln_pds_tot_iunits_reqd=soln_pds_tot_iunits_reqd,
        soln_ref_tot_iunits_reqd=soln_ref_tot_iunits_reqd,
        conv_ref_tot_iunits=conv_ref_tot_iunits,
        soln_pds_new_iunits_reqd=self.ua.soln_pds_new_iunits_reqd(),
        soln_ref_new_iunits_reqd=self.ua.soln_ref_new_iunits_reqd(),
        conv_ref_new_iunits=self.ua.conv_ref_new_iunits(),
        fc_convert_iunit_factor=1.0)

    self.oc = operatingcost.OperatingCost(ac=self.ac,
        soln_net_annual_funits_adopted=soln_net_annual_funits_adopted,
        soln_pds_tot_iunits_reqd=soln_pds_tot_iunits_reqd,
        soln_ref_tot_iunits_reqd=soln_ref_tot_iunits_reqd,
        conv_ref_annual_tot_iunits=self.ua.conv_ref_annual_tot_iunits(),
        soln_pds_annual_world_first_cost=self.fc.soln_pds_annual_world_first_cost(),
        soln_ref_annual_world_first_cost=self.fc.soln_ref_annual_world_first_cost(),
        conv_ref_annual_world_first_cost=self.fc.conv_ref_annual_world_first_cost(),
        single_iunit_purchase_year=2017,
        soln_pds_install_cost_per_iunit=self.fc.soln_pds_install_cost_per_iunit(),
        conv_ref_install_cost_per_iunit=self.fc.conv_ref_install_cost_per_iunit(),
        conversion_factor=1.0)

    self.c4 = ch4calcs.CH4Calcs(ac=self.ac,
        soln_net_annual_funits_adopted=soln_net_annual_funits_adopted)

    self.c2 = co2calcs.CO2Calcs(ac=self.ac,
        ch4_ppb_calculator=self.c4.ch4_ppb_calculator(),
        soln_pds_net_grid_electricity_units_saved=self.ua.soln_pds_net_grid_electricity_units_saved(),
        soln_pds_net_grid_electricity_units_used=self.ua.soln_pds_net_grid_electricity_units_used(),
        soln_pds_direct_co2_emissions_saved=self.ua.soln_pds_direct_co2_emissions_saved(),
        soln_pds_direct_ch4_co2_emissions_saved=self.ua.soln_pds_direct_ch4_co2_emissions_saved(),
        soln_pds_direct_n2o_co2_emissions_saved=self.ua.soln_pds_direct_n2o_co2_emissions_saved(),
        soln_pds_new_iunits_reqd=self.ua.soln_pds_new_iunits_reqd(),
        soln_ref_new_iunits_reqd=self.ua.soln_ref_new_iunits_reqd(),
        conv_ref_new_iunits=self.ua.conv_ref_new_iunits(),
        conv_ref_grid_CO2_per_KWh=self.ef.conv_ref_grid_CO2_per_KWh(),
        conv_ref_grid_CO2eq_per_KWh=self.ef.conv_ref_grid_CO2eq_per_KWh(),
        soln_net_annual_funits_adopted=soln_net_annual_funits_adopted,
        fuel_in_liters=False)

    self.r2s = rrs.RRS(total_energy_demand=ref_tam_per_region.loc[2014, 'World'],
        soln_avg_annual_use=self.ac.soln_avg_annual_use,
        conv_avg_annual_use=self.ac.conv_avg_annual_use)

