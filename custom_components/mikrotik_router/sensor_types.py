"""Definitions for sensor entities."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import EntityCategory
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
    SensorEntityDescription,
)
from homeassistant.const import (
    PERCENTAGE,
    REVOLUTIONS_PER_MINUTE,
    UnitOfTemperature,
    UnitOfDataRate,
    UnitOfInformation,
    UnitOfElectricPotential,
    UnitOfElectricCurrent,
    UnitOfPower,
)

from .const import DOMAIN

DEVICE_ATTRIBUTES_IFACE = [
    "running",
    "enabled",
    "comment",
    "client-ip-address",
    "client-mac-address",
    "port-mac-address",
    "last-link-down-time",
    "last-link-up-time",
    "link-downs",
    "actual-mtu",
    "type",
    "name",
]

DEVICE_ATTRIBUTES_IFACE_ETHER = [
    "status",
    "auto-negotiation",
    "rate",
    "full-duplex",
    "default-name",
    "poe-out",
]

DEVICE_ATTRIBUTES_IFACE_SFP = [
    "status",
    "auto-negotiation",
    "advertising",
    "link-partner-advertising",
    "sfp-temperature",
    "sfp-supply-voltage",
    "sfp-module-present",
    "sfp-tx-bias-current",
    "sfp-tx-power",
    "sfp-rx-power",
    "sfp-rx-loss",
    "sfp-tx-fault",
    "sfp-type",
    "sfp-connector-type",
    "sfp-vendor-name",
    "sfp-vendor-part-number",
    "sfp-vendor-revision",
    "sfp-vendor-serial",
    "sfp-manufacturing-date",
    "eeprom-checksum",
]

DEVICE_ATTRIBUTES_IFACE_WIRELESS = [
    "ssid",
    "mode",
    "radio-name",
    "interface-type",
    "country",
    "installation",
    "antenna-gain",
    "frequency",
    "band",
    "channel-width",
    "secondary-frequency",
    "wireless-protocol",
    "rate-set",
    "distance",
    "tx-power-mode",
    "vlan-id",
    "wds-mode",
    "wds-default-bridge",
    "bridge-mode",
    "hide-ssid",
]

DEVICE_ATTRIBUTES_CLIENT_TRAFFIC = [
    "address",
    "mac-address",
    "host-name",
    "authorized",
    "bypassed",
]
DEVICE_ATTRIBUTES_GPS = [
    "valid",
    "latitude",
    "longitude",
    "altitude",
    "speed",
    "destination-bearing",
    "true-bearing",
    "magnetic-bearing",
    "satellites",
    "fix-quality",
    "horizontal-dilution",
]


@dataclass
class MikrotikSensorEntityDescription(SensorEntityDescription):
    """Class describing mikrotik entities."""

    ha_group: str | None = None
    ha_connection: str | None = None
    ha_connection_value: str | None = None
    data_path: str | None = None
    data_attribute: str | None = None
    data_name: str | None = None
    data_name_comment: bool = False
    data_uid: str | None = None
    data_reference: str | None = None
    data_attributes_list: List = field(default_factory=lambda: [])
    func: str = "MikrotikSensor"


SENSOR_TYPES: tuple[MikrotikSensorEntityDescription, ...] = (
    MikrotikSensorEntityDescription(
        key="system_temperature",
        name="Temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_display_precision=0,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="temperature",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_voltage",
        name="Voltage",
        icon="mdi:lightning-bolt",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        suggested_unit_of_measurement=UnitOfElectricPotential.VOLT,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="voltage",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_cpu-temperature",
        name="CPU temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_display_precision=0,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="cpu-temperature",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_switch-temperature",
        name="Switch temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_display_precision=0,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="switch-temperature",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_board-temperature1",
        name="Board temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_display_precision=0,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="board-temperature1",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_phy-temperature",
        name="PHY temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_display_precision=0,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="phy-temperature",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_power-consumption",
        name="Power consumption",
        icon="mdi:transmission-tower",
        native_unit_of_measurement=UnitOfPower.WATT,
        suggested_unit_of_measurement=UnitOfPower.WATT,
        suggested_display_precision=0,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="power-consumption",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_poe_out_consumption",
        name="PoE out power consumption",
        icon="mdi:flash",
        native_unit_of_measurement=UnitOfPower.WATT,
        suggested_unit_of_measurement=UnitOfPower.WATT,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="poe-out-consumption",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_fan1-speed",
        name="Fan1 speed",
        icon="mdi:fan",
        native_unit_of_measurement=REVOLUTIONS_PER_MINUTE,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="fan1-speed",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_fan2-speed",
        name="Fan2 speed",
        icon="mdi:fan",
        native_unit_of_measurement=REVOLUTIONS_PER_MINUTE,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="fan2-speed",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_fan3-speed",
        name="Fan3 speed",
        icon="mdi:fan",
        native_unit_of_measurement=REVOLUTIONS_PER_MINUTE,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="fan3-speed",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_fan4-speed",
        name="Fan4 speed",
        icon="mdi:fan",
        native_unit_of_measurement=REVOLUTIONS_PER_MINUTE,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="fan4-speed",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_poe_out_consumption",
        name="PoE out power consumption",
        icon="mdi:transmission-tower",
        native_unit_of_measurement=UnitOfPower.WATT,
        suggested_unit_of_measurement=UnitOfPower.WATT,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="poe-out-consumption",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_psu1_current",
        name="PSU 1 power consumption",
        icon="mdi:lightning-bolt-circle",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        suggested_unit_of_measurement=UnitOfElectricCurrent.MILLIAMPERE,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="psu1-current",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_psu1_voltage",
        name="PSU 1 Voltage",
        icon="mdi:lightning-bolt",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        suggested_unit_of_measurement=UnitOfElectricPotential.VOLT,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="psu1-voltage",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_psu2_current",
        name="PSU 2 power consumption",
        icon="mdi:lightning-bolt-circle",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        suggested_unit_of_measurement=UnitOfElectricCurrent.MILLIAMPERE,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="psu2-current",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_psu2_voltage",
        name="PSU 2 Voltage",
        icon="mdi:lightning-bolt",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        suggested_unit_of_measurement=UnitOfElectricPotential.VOLT,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="psu2-voltage",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_uptime",
        name="Uptime",
        icon=None,
        native_unit_of_measurement=None,
        device_class=SensorDeviceClass.TIMESTAMP,
        state_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="resource",
        data_attribute="uptime",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_cpu-load",
        name="CPU load",
        icon="mdi:speedometer",
        native_unit_of_measurement=PERCENTAGE,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="resource",
        data_attribute="cpu-load",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_memory-usage",
        name="Memory usage",
        icon="mdi:memory",
        native_unit_of_measurement=PERCENTAGE,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="resource",
        data_attribute="memory-usage",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_hdd-usage",
        name="HDD usage",
        icon="mdi:harddisk",
        native_unit_of_measurement=PERCENTAGE,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="resource",
        data_attribute="hdd-usage",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_clients-wired",
        name="Wired clients",
        icon="mdi:lan",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="resource",
        data_attribute="clients_wired",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_clients-wireless",
        name="Wireless clients",
        icon="mdi:wifi",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="resource",
        data_attribute="clients_wireless",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_captive-authorized",
        name="Captive portal clients",
        icon="mdi:key-wireless",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="resource",
        data_attribute="captive_authorized",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_gps-latitude",
        name="Latitude",
        icon="mdi:latitude",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="gps",
        data_attribute="latitude",
        data_name="",
        data_uid="",
        data_reference="",
        data_attributes_list=DEVICE_ATTRIBUTES_GPS,
    ),
    MikrotikSensorEntityDescription(
        key="system_gps-longitude",
        name="Longitude",
        icon="mdi:longitude",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="gps",
        data_attribute="longitude",
        data_name="",
        data_uid="",
        data_reference="",
        data_attributes_list=DEVICE_ATTRIBUTES_GPS,
    ),
    MikrotikSensorEntityDescription(
        key="traffic_tx",
        name="TX",
        icon="mdi:upload-network-outline",
        native_unit_of_measurement=UnitOfDataRate.BYTES_PER_SECOND,
        suggested_unit_of_measurement=UnitOfDataRate.KILOBYTES_PER_SECOND,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="data__default-name",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__port-mac-address",
        data_path="interface",
        data_attribute="tx",
        data_name="default-name",
        data_uid="",
        data_reference="default-name",
        data_attributes_list=DEVICE_ATTRIBUTES_IFACE,
        func="MikrotikInterfaceTrafficSensor",
    ),
    MikrotikSensorEntityDescription(
        key="traffic_rx",
        name="RX",
        icon="mdi:download-network-outline",
        native_unit_of_measurement=UnitOfDataRate.BYTES_PER_SECOND,
        suggested_unit_of_measurement=UnitOfDataRate.KILOBYTES_PER_SECOND,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="data__default-name",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__port-mac-address",
        data_path="interface",
        data_attribute="rx",
        data_name="default-name",
        data_uid="",
        data_reference="default-name",
        data_attributes_list=DEVICE_ATTRIBUTES_IFACE,
        func="MikrotikInterfaceTrafficSensor",
    ),
    MikrotikSensorEntityDescription(
        key="tx-total",
        name="TX total",
        icon="mdi:upload-network",
        native_unit_of_measurement=UnitOfInformation.BYTES,
        suggested_unit_of_measurement=UnitOfInformation.GIGABYTES,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.DATA_SIZE,
        state_class=SensorStateClass.TOTAL_INCREASING,
        entity_category=None,
        ha_group="data__default-name",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__port-mac-address",
        data_path="interface",
        data_attribute="tx-current",
        data_name="default-name",
        data_uid="",
        data_reference="default-name",
        data_attributes_list=DEVICE_ATTRIBUTES_IFACE,
        func="MikrotikInterfaceTrafficSensor",
    ),
    MikrotikSensorEntityDescription(
        key="rx-total",
        name="RX total",
        icon="mdi:download-network",
        native_unit_of_measurement=UnitOfInformation.BYTES,
        suggested_unit_of_measurement=UnitOfInformation.GIGABYTES,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.DATA_SIZE,
        state_class=SensorStateClass.TOTAL_INCREASING,
        entity_category=None,
        ha_group="data__default-name",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__port-mac-address",
        data_path="interface",
        data_attribute="rx-current",
        data_name="default-name",
        data_uid="",
        data_reference="default-name",
        data_attributes_list=DEVICE_ATTRIBUTES_IFACE,
        func="MikrotikInterfaceTrafficSensor",
    ),
    MikrotikSensorEntityDescription(
        key="client_traffic_lan_tx",
        name="LAN TX",
        icon="mdi:upload-network",
        native_unit_of_measurement=UnitOfDataRate.BYTES_PER_SECOND,
        suggested_unit_of_measurement=UnitOfDataRate.KILOBYTES_PER_SECOND,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__mac-address",
        data_path="client_traffic",
        data_attribute="lan-tx",
        data_name="host-name",
        data_uid="",
        data_reference="mac-address",
        data_attributes_list=DEVICE_ATTRIBUTES_CLIENT_TRAFFIC,
        func="MikrotikClientTrafficSensor",
    ),
    MikrotikSensorEntityDescription(
        key="client_traffic_lan_rx",
        name="LAN RX",
        icon="mdi:download-network",
        native_unit_of_measurement=UnitOfDataRate.BYTES_PER_SECOND,
        suggested_unit_of_measurement=UnitOfDataRate.KILOBYTES_PER_SECOND,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__mac-address",
        data_path="client_traffic",
        data_attribute="lan-rx",
        data_name="host-name",
        data_uid="",
        data_reference="mac-address",
        data_attributes_list=DEVICE_ATTRIBUTES_CLIENT_TRAFFIC,
        func="MikrotikClientTrafficSensor",
    ),
    MikrotikSensorEntityDescription(
        key="client_traffic_wan_tx",
        name="WAN TX",
        icon="mdi:upload-network",
        native_unit_of_measurement=UnitOfDataRate.BYTES_PER_SECOND,
        suggested_unit_of_measurement=UnitOfDataRate.KILOBYTES_PER_SECOND,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__mac-address",
        data_path="client_traffic",
        data_attribute="wan-tx",
        data_name="host-name",
        data_uid="",
        data_reference="mac-address",
        data_attributes_list=DEVICE_ATTRIBUTES_CLIENT_TRAFFIC,
        func="MikrotikClientTrafficSensor",
    ),
    MikrotikSensorEntityDescription(
        key="client_traffic_wan_rx",
        name="WAN RX",
        icon="mdi:download-network",
        native_unit_of_measurement=UnitOfDataRate.BYTES_PER_SECOND,
        suggested_unit_of_measurement=UnitOfDataRate.KILOBYTES_PER_SECOND,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__mac-address",
        data_path="client_traffic",
        data_attribute="wan-rx",
        data_name="host-name",
        data_uid="",
        data_reference="mac-address",
        data_attributes_list=DEVICE_ATTRIBUTES_CLIENT_TRAFFIC,
        func="MikrotikClientTrafficSensor",
    ),
    MikrotikSensorEntityDescription(
        key="client_traffic_tx",
        name="TX",
        icon="mdi:upload-network",
        native_unit_of_measurement=UnitOfDataRate.BYTES_PER_SECOND,
        suggested_unit_of_measurement=UnitOfDataRate.KILOBYTES_PER_SECOND,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__mac-address",
        data_path="client_traffic",
        data_attribute="tx",
        data_name="host-name",
        data_uid="",
        data_reference="mac-address",
        data_attributes_list=DEVICE_ATTRIBUTES_CLIENT_TRAFFIC,
        func="MikrotikClientTrafficSensor",
    ),
    MikrotikSensorEntityDescription(
        key="client_traffic_rx",
        name="RX",
        icon="mdi:download-network",
        native_unit_of_measurement=UnitOfDataRate.BYTES_PER_SECOND,
        suggested_unit_of_measurement=UnitOfDataRate.KILOBYTES_PER_SECOND,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__mac-address",
        data_path="client_traffic",
        data_attribute="rx",
        data_name="host-name",
        data_uid="",
        data_reference="mac-address",
        data_attributes_list=DEVICE_ATTRIBUTES_CLIENT_TRAFFIC,
        func="MikrotikClientTrafficSensor",
    ),
    MikrotikSensorEntityDescription(
        key="environment",
        name="",
        icon="mdi:clipboard-list",
        native_unit_of_measurement="",
        device_class=None,
        state_class=None,
        entity_category=None,
        ha_group="Environment",
        ha_connection=DOMAIN,
        ha_connection_value="Environment",
        data_path="environment",
        data_attribute="value",
        data_name="name",
        data_uid="name",
        data_reference="name",
    ),
)

SENSOR_SERVICES = []
