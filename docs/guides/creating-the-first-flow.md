---
title: "Creating the First Flow"
source: https://automagic4android.com/creating_first_flow_en.html
archived: 2019-04-24
archive_url: https://web.archive.org/web/20190424180706/https://automagic4android.com/creating_first_flow_en.html
category: help
---

# Creating the First Flow

This tutorial is a guide to build a basic flow that shows every 5 minutes a text on the display.
The first version shows the text "Hello Automagic". The slightly more advanced version displays the formatted current time.

## Step 1 - Creating a New Flow

Every automated processes in Automagic is modeled as a flow so we have to create a new empty flow first.
Please start Automagic and ensure that you are positioned on the flow list as shown in the following screen:

![Flow List Menu](../assets/screenshots/en/notification_flow/S02_FlowListMenu_Overlay.png)

Select the red floating action button **+** to create a flow.

## Step 2 - Adding the Trigger

In this step we are going to add a **trigger** that will execute the flow every 5 minutes.

![Empty Flow](../assets/screenshots/en/notification_flow/S03_FlowEmpty_Overlay.png)

The gray rounded rectangle contains the triggers that automatically execute a flow. The rectangle is empty since we did not yet define the trigger to use.
Press the list icon above the rounded rectangle to show a list of existing triggers.

![Existing Trigger Selection](../assets/screenshots/en/notification_flow/S04_Flow_SelectTrigger_Overlay.png)

The list with existing triggers is displayed on the screen.
A 5 minute trigger does not exist yet in the list so we have to create a new one.
Press the **New** button to create a new trigger.

![Trigger Type Selection](../assets/screenshots/en/notification_flow/S05_Flow_SelectTriggerType_Overlay.png)

The list of all available types of triggers is shown.
Scroll down and select the trigger type **Periodic Timer**.

![Edit Trigger](../assets/screenshots/en/notification_flow/S06_Flow_EditTrigger_Overlay.png)

You can change the values in this screen to define how often the trigger will execute the flow by changing the interval to a different value like "2m" or "2m 30s". A help screen with a description of valid time intervals in Automagic can be accessed using the blue question mark icon.
There is also a more detailed description of each trigger type available using the **?**-button.

You can use the default settings for this trigger and press the **Save** button.

## Step 3 - Adding the Action

In this step we are going to add an **action** that will display the text "Hello Automagic" on the screen.

![Adding the Container](../assets/screenshots/en/notification_flow/S07_Flow_AddActionContainer_Overlay.png)

Press and hold the plus icon under the trigger and drag the icon down to a free area to add a new container for an action to the flow.

![Selecting the Action Container](../assets/screenshots/en/notification_flow/S08_Flow_SelectContainerType_Overlay.png)

Select the container type **Action**.

![Creating a new Action](../assets/screenshots/en/notification_flow/S09_Flow_SelectAction_Overlay.png)

A list with existing actions is displayed.
Press the **New** button to create a new action.

![Selecting the Action Type](../assets/screenshots/en/notification_flow/S10_Flow_SelectActionType_Overlay.png)

The list of all available action types is displayed.
Scroll down and select the type **Notification on Screen** to display a simple text that automatically vanishes after a few seconds.

![Entering Hello Automagic](../assets/screenshots/en/notification_flow/S11_Flow_EditActionFixText_Overlay.png)

Enter the text "Hello Automagic".
Note that the name of the action is automatically adjusted to reflect your settings.
The name of the action must be unique within Automagic since an action is identified by its name.
Automagic will check if an action with the same name already exists and allows to reuse an already existing action.

![Executing the Action](../assets/screenshots/en/notification_flow/S12_Flow_EditActionFixTextMenu_Overlay.png)

It is often required to test if the settings of an action are correct and the action does what you want.
Open the menu and press the **Execute** menu item to test the action.

The action is executed in complete isolation. This means that the rest of the flow is not executed. The action itself is executed for real, this means that an action that is configured to delete a file on the device will really delete the file when executed using the **Execute** menu item.

![Notification Hello Automagic](../assets/screenshots/en/notification_flow/S13_Flow_EditActionFixExecute_Overlay.png)

Ensure that the displayed text matches your expectations.
Press the **Save** button to accept the values of the action.

![Action Created](../assets/screenshots/en/notification_flow/S14_Flow_ActionFixTextCreated_Overlay.png)

The action is now displayed in the flow.

## Step 4- Manually Starting a Flow

In this step we are going to add an **action** that will display the text "Hello Automagic" on the screen.

![Executing the Flow](../assets/screenshots/en/notification_flow/S15_Flow_Menu_Overlay.png)

Open the menu and select the **Execute** menu item.

![Flow Executing](../assets/screenshots/en/notification_flow/S16_Flow_TestExecute_Overlay.png)

The flow displays the currently executing element in red. There also exists a menu item **Stop** to interrupt a flow if you see that there is a problem and you want to stop the flow early.
The text "Hello Automagic" should be shown as soon as the action "Notification on Screen" is reached.

You can now enable the flow by turning the switch button to ON.
The flow is registered in the system and will be executed every 5 minutes automatically from now on.

![Flow Enabled](../assets/screenshots/en/notification_flow/S17_Flow_Enabled_Overlay.png)

Note that the container with the trigger changes the background color when the flow is enabled.

You can rename a flow opening the menu and selecting **Rename**.

![Renaming the Flow](../assets/screenshots/en/notification_flow/S18_Flow_Rename_Overlay.png)

Rename the flow to "Notification Flow". The name of a flow must be unique within Automagic.

## Step 5 - Extend the Flow to Show the Current Time

In this step we are going to enhance the flow to show the current time instead of the static text "Hello Automagic".

The time (and optionally the date) can be shown using a variable. Almost all text fields allow to define a dynamic text by using a variable in curly braces **{}**.

![Editing the Action](../assets/screenshots/en/notification_flow/S19_Flow_ActionSelected_Overlay.png)

Press the edit icon to directly open the editing screen of the action.

![Opening the Variable Chooser](../assets/screenshots/en/notification_flow/S20_Flow_EditActionItIs_Overlay.png)

Change the text to "It is " then open the menu and select the item **Select Variable**.

![Selecting the Variable](../assets/screenshots/en/notification_flow/S21_Flow_EditActionItIsVariablePicker_Overlay.png)

Automagic determines the variables that are likely available when the flow execution reaches this action.
One of the variables available in all flows is the variable **triggertime**. It contains the date and time when the trigger has been executed.
The first five entries in the list show usage examples of this variable with three different formatting options. The first entry formats the time using the 24-hour format with minutes and seconds.

Select the first entry of the list.

![Variable copied to Clipboard](../assets/screenshots/en/notification_flow/S22_Flow_EditActionSelectedVariable_Overlay.png)

Notice that the selected variable is copied to the clipboard.

![Pasting the Variable](../assets/screenshots/en/notification_flow/S23_Flow_EditActionPasteVariable_Overlay.png)

Long-press the text field to paste the contents of the clipboard into the text field.

![Variable Rendering](../assets/screenshots/en/notification_flow/S24_Flow_EditActionPasteVariableDone_Overlay.png)

The variable is rendered in blue to indicate that this part of the text is dynamic and will be replaced when the action is executed.

![Executing the Action](../assets/screenshots/en/notification_flow/S25_Flow_EditActionItIsTimeExecuted_Overlay.png)

Open the menu and execute the action. The current time should be displayed.

![Final Flow](../assets/screenshots/en/notification_flow/S26_Flow_ItIsTimeEnhanced_Overlay.png)

You can now save the action. Notice that the action name has been automatically adjusted to reflect the new text of the action.

---

[← Indeks panduan](README.md) · [Peta dokumentasi](../README.md)
