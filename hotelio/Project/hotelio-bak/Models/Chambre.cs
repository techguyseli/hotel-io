namespace hotelio.Models
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Data.Entity.Spatial;

    public partial class Chambre
    {
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2214:DoNotCallOverridableMethodsInConstructors")]
        public Chambre()
        {
            ChambresReservees = new HashSet<ChambresReservee>();
        }

        [Key]
        public int idChambre { get; set; }

        public int? idHotel { get; set; }

        [Required]
        [StringLength(20)]
        public string typeChambre { get; set; }

        public double prix { get; set; }

        public int nbrCouchages { get; set; }

        public bool litDePlus { get; set; }

        public int nbrChambres { get; set; }

        public virtual Hotel Hotel { get; set; }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<ChambresReservee> ChambresReservees { get; set; }
    }
}
