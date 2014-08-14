/**
 * Created by Heta on 13-08-2014.
 */
function validation()
{
    alert("Hello")
    var mob=document.getElementsByClassName(c2);
    alert("Hello");
    if(isNaN(mob.value))
    {
        alert("Please enter digit only");
        mob.value="";
        mob.focus();
        return false;
    }
    else if(!(mob.value.length == 10))
    {
        alert("Please enter only 10 digit")
        mob.value="";
        mob.focus();
        return false;
    }
}