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
    
    public partial class option
    {
        public option()
        {
            this.hotels = new HashSet<hotel>();
        }
    
        public int option_id { get; set; }
        public string hotel_option { get; set; }
    
        public virtual ICollection<hotel> hotels { get; set; }
    }
}
