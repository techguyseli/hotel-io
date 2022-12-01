namespace hotelio.Models
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Data.Entity.Spatial;

    public partial class Reservation
    {
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2214:DoNotCallOverridableMethodsInConstructors")]
        public Reservation()
        {
            ChambresReservees = new HashSet<ChambresReservee>();
        }

        [Key]
        public int idReservation { get; set; }

        public int? idUser { get; set; }

        [Column(TypeName = "date")]
        public DateTime dateArrivee { get; set; }

        [Column(TypeName = "date")]
        public DateTime dateDepart { get; set; }

        [StringLength(20)]
        public string resevationStatut { get; set; }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<ChambresReservee> ChambresReservees { get; set; }

        public virtual User User { get; set; }
    }
}
