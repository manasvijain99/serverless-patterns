#!/usr/bin/env python3
import aws_cdk as cdk

from eventbridge_schedule_remove_onetime_schedule_to_sns_cdk_python.eventbridge_schedule_remove_onetime_schedule_to_sns_cdk_python_stack import EventbridgeOnetimeScheduleRemoveToSnsCdkPythonStack



app = cdk.App()
EventbridgeOnetimeScheduleRemoveToSnsCdkPythonStack(app, "EventbridgeOnetimeScheduleRemoveToSnsCdkPythonStack")

app.synth()