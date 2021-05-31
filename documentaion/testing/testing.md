# Testing

[back to README.md file](https://github.com/leeton1412/mile-stone/master/README.md)

## Table of Content

1. [DevTools](#devtools)
2. [Manual Testing](#manual-testing)
3. [Automated Testing](#automated-testing)
4. [User testing](#user-testing)




## DevTools

* Testing the responsiveness of the web app.
    * Major issues discovered with mobile nav. Time issues means this may not be rectified in time.
    * I used Bootstrap to ensure I have reactive columns on different screen sizes. As before some issues have been identified for fixing.
* Testing that the css is targeting the relevant html code.
    * As an outcome the webiste is responsive on all screen sizes.
    * AllAuth Templates still need customizing 
* Console Debugging
    * As an outcome I was able to see whether my Javascript functions were being called and were executing properly by displaying a console.log value in my console.
    * I noted that a Favicon was missing and was able to fix this by adding a favicon script and images. 
    * I noted that there is an issue with checkout view, save_info not saving and preventing delivery information being save.


## Manual Testing

* Home Page
   * Search icon lower than search bar.
   * Banner not covering Full Screen.
   * Remove second level due to product type -on brownies and cakes:

   ![Search bar](https://github.com/leeton1412/mile-stone/blob/master/documentaion/testing/images/Banner_image.png)<br>


   ![Product Drop](https://github.com/leeton1412/mile-stone/blob/master/documentaion/testing/images/Product_drop.png)

* Products
    * Images to show on to product page.
    * Change colour of text to show better.
    * Change colour of text to show better.

    ![Images](https://github.com/leeton1412/mile-stone/blob/master/documentaion/testing/images/Products_with_images_missing.png)<br>


    ![Text Problem](https://github.com/leeton1412/mile-stone/blob/master/documentaion/testing/images/Text_not_showing.png)


* Products Detail
    * Buttons to be swapped. 

    ![Buttons](https://github.com/leeton1412/mile-stone/blob/master/documentaion/testing/images/Buttons_to_be_swapped.png)

* Bag
    * Text not displaying due to no background on text
    * Carriage charge not displaying on basket.
    * Quantity bar higher than other elements creating responsive issues
    * Table no longer fits after static submit mobile view

    ![Text Problem](https://github.com/leeton1412/mile-stone/blob/master/documentaion/testing/images/Text_not_showing_in_basket.png)<br>


    ![Charge](https://github.com/leeton1412/mile-stone/blob/master/documentaion/testing/images/Carrier_charge_on_basket.png)

* Sign Up Page 
    * Unable to see text or where email/user name needs to be added – the forgot password and sign in to look the same.

    ![Sign in](https://github.com/leeton1412/mile-stone/blob/master/documentaion/testing/images/sign_in_page.png)

* Profile 
    * When logged in and on my profile you can update your details due to background unable to see what you are typing.
    * Major error with information not being saved.
    * Remove button not functioning 

    ![Sign in](https://github.com/leeton1412/mile-stone/blob/master/documentaion/testing/images/My_Profile.png)

* Checkout 
    * Within the checkout window you are unable to see text due to colour.
    * Within the country field you must input country code. Django countries import error 
    * Above payment you are unable to see “Save This Information” – also a little confusing with the payment header and looks like where you should put card details.
    * Payment needs zipcode

    ![Checkout](https://github.com/leeton1412/mile-stone/blob/master/documentaion/testing/images/Check_out_window.png)<br>


    ![Checkout](https://github.com/leeton1412/mile-stone/blob/master/documentaion/testing/images/PaymentOnCheckout.png) 

* Order Confirmation
    * Text not able to be displayed due to colour
    * At the bottom of the confirmed checkout page shows billing information but no data below this.

    ![Order](https://github.com/leeton1412/mile-stone/blob/master/documentaion/testing/images/PaymentOnCheckout.png)<br>


    ![Order](https://github.com/leeton1412/mile-stone/blob/master/documentaion/testing/images/ConfirmedOrderPageMarginIssue.png)<br>


    ![Order](https://github.com/leeton1412/mile-stone/blob/master/documentaion/testing/images/ConfirmedOrderPageBillingInformationNoData.png)

* Mobile Home page
    * After Static commit issues have shown up in regards to navbar not staying inline. This has caused issues and due to having to submit cannot be rectified.

    ![Nav Issue](https://github.com/leeton1412/mile-stone/blob/master/documentaion/testing/images/MobileViewHomepage.png)<br>


    ![Nav Issue](https://github.com/leeton1412/mile-stone/blob/master/documentaion/testing/images/MobileViewConfirmationError.png)



















   