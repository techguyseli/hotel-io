//------------------------------------------------------------------------------
// <auto-generated>
//    This code was generated from a template.
//
//    Manual changes to this file may cause unexpected behavior in your application.
//    Manual changes to this file will be overwritten if the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace hotelio.Models
{
    using System;
    using System.Collections.Generic;
    
    public partial class user
    {
        public user()
        {
            this.comments = new HashSet<comment>();
            this.reservations = new HashSet<reservation>();
        }
    
        public int user_id { get; set; }
        public string email { get; set; }
        public string password { get; set; }
        public string first_name { get; set; }
        public string last_name { get; set; }
        public string adress { get; set; }
        public string phone { get; set; }
        public string role { get; set; }
    
        public virtual ICollection<comment> comments { get; set; }
        public virtual ICollection<reservation> reservations { get; set; }
    }
}
