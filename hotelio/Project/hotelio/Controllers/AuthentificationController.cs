using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace hotelio.Controllers
{
    public class AuthentificationController : Controller
    {
        // GET: Authentification
        [HttpGet]
        public ActionResult Login()
        {
            return View();
        }

        [HttpGet]
        public ActionResult Register()
        {
            return View();
        }

        [HttpPost]
        public ActionResult Login_Post()
        {
            return Redirect("/Home/Index");
        }

        [HttpPost]
        public ActionResult Register_Post()
        {
            return View();
        }
    }
}